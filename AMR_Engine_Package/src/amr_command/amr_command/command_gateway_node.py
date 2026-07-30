"""
Arbitrates commands from the remote operator console (and future input
sources, e.g. a joystick), forwards validated decisions to amr_engine, and
streams live telemetry (map, battery, lift/fault status) out over a websocket.
"""
import asyncio
import threading
import math
import time
import os
import re
import json


import rclpy
from rclpy.node import Node
from rclpy.time import Time
from rclpy.qos import (
    DurabilityPolicy,
    HistoryPolicy,
    QoSProfile,
    ReliabilityPolicy,
)

from geometry_msgs.msg import Twist, PoseStamped
from nav_msgs.msg import OccupancyGrid, Odometry, Path
from sensor_msgs.msg import LaserScan

from nav2_msgs.msg import CostmapFilterInfo

from rcl_interfaces.srv import GetParameters

from slam_toolbox.srv import (
    SerializePoseGraph,
    DeserializePoseGraph
)

from amr_command.map_encoder import encode_occupancy_grid
from amr_command.websocket_server import WebsocketServer
from amr_command.path_executor import PathExecutor
from amr_command import keepout_zones



class OperatorInputArbiter:

    def __init__(self):
        self._linear = 0.0
        self._angular = 0.0
        self._last_command_time = None
        self._lock = threading.Lock()

    def submit_command(self, source: str, linear: float, angular: float):
        with self._lock:
            self._linear = linear
            self._angular = angular
            self._last_command_time = time.monotonic()

    def get_active_command(self):
        with self._lock:
            return (
                self._linear,
                self._angular,
                self._last_command_time,
            )


class CommandGatewayNode(Node):

    def __init__(self):
        super().__init__("amr_command")
        self.get_logger().info("CommandGatewayNode started")

        self.websocket_server = WebsocketServer()
        self.websocket_server._on_message_cb = self._on_ws_frame

        self.arbiter = OperatorInputArbiter()

        # Executes operator-drawn paths via Nav2. Reports progress back to the
        # console through _broadcast, which is safe to call before the
        # websocket loop exists.
        self.path_executor = PathExecutor(self, self._broadcast)

        self._latest_pose = None

        self.declare_parameter(
            "maps_directory",
            # Absolute by default. We list this directory relative to our own
            # process CWD, but slam_toolbox writes the file relative to *its*
            # CWD -- if the two are launched from different places a
            # "successful" save never appears in the list and Load's existence
            # check fails. An absolute path removes the ambiguity, which is
            # also why the filenames handed to the services below are absolute.
            os.path.join(os.path.expanduser("~"), ".ros", "amr_maps"),
        )

        # Normalise whatever we were handed, so a relative override still
        # resolves to an absolute path instead of quietly reintroducing the
        # CWD mismatch above.
        self.maps_directory = os.path.abspath(
            os.path.expanduser(
                self.get_parameter("maps_directory").value
            )
        )

        self.declare_parameter(
            "paths_directory",
            os.path.join(os.path.expanduser("~"), ".ros", "amr_paths"),
        )

        # Same treatment as maps_directory: paths are written and read back by
        # name, so a relative default would resolve against whatever CWD the
        # gateway happened to be launched from.
        self.paths_directory = os.path.abspath(
            os.path.expanduser(
                self.get_parameter("paths_directory").value
            )
        )

        self.declare_parameter(
            "zones_directory",
            os.path.join(os.path.expanduser("~"), ".ros", "amr_zones"),
        )

        self.zones_directory = os.path.abspath(
            os.path.expanduser(
                self.get_parameter("zones_directory").value
            )
        )

        # How far to grow each zone when rasterising it. Nav2 runs costmap
        # filters after the layer stack, so the inflation layer never sees
        # keep-out cells: without a margin here the planner keeps the robot's
        # *centre* out of a zone while its body clips the corner. Defaults to
        # the inscribed radius of the footprint in nav2_params.yaml.
        self.declare_parameter("zone_margin", 0.4)

        self.zone_margin = float(
            self.get_parameter("zone_margin").value
        )

        try:
            self.zone_store = keepout_zones.ZoneStore(self.zones_directory)
        except Exception as e:
            # A corrupt store must be loud: silently starting with zero zones
            # would mean publishing an empty mask and driving through areas
            # the operator believes are still blocked.
            self.get_logger().error(
                f"Could not read keep-out zones from {self.zones_directory}: "
                f"{e}. Starting with no zones -- previously saved zones are "
                f"NOT being enforced."
            )
            self.zone_store = keepout_zones.ZoneStore(
                self.zones_directory,
                filename="zones.recovered.json",
            )

        # --- teleop collision guard ---------------------------------------
        #
        # Nav2 already refuses to drive an autonomous goal into an obstacle:
        # the costmaps mark it and DWB's BaseObstacle critic scores those
        # trajectories out. Teleop has no such protection -- it goes straight
        # from a browser button to /cmd_vel, bypassing Nav2 entirely -- so an
        # operator holding "forward" drives the robot into a wall. This is
        # that missing check.

        self.declare_parameter("collision_stop_distance", 0.35)
        self.declare_parameter("collision_sector_deg", 60.0)

        self.collision_stop_distance = float(
            self.get_parameter("collision_stop_distance").value
        )

        self.collision_sector_rad = math.radians(
            float(self.get_parameter("collision_sector_deg").value)
        )

        self._latest_scan = None

        # Rate-limits the "blocked" frame so holding the button against a
        # wall does not flood the socket.
        self._last_block_notice = 0.0

        # How far a drawn path must stay from a wall. Under the footprint's
        # 0.4 m inscribed radius on purpose: at a full 0.4 m the check refuses
        # perfectly drivable paths down a narrow aisle, and Nav2's own
        # costmap is the thing that ultimately keeps the robot off the wall.
        # This check exists to catch the grossly-through-a-wall case early.
        self.declare_parameter("obstacle_margin", 0.30)

        self.obstacle_margin = float(
            self.get_parameter("obstacle_margin").value
        )

        # Geometry of the most recent /map, so a zone edit can be rasterised
        # onto the same grid without waiting for the next map update.
        self._latest_map_info = None

        # Occupancy of the most recent /map, plus the inflated obstacle mask
        # derived from it. The mask is built lazily on the first path check
        # after a map arrives rather than on every update: maps arrive every
        # couple of seconds whether or not anyone is drawing a path, and
        # inflating a large grid is not free.
        self._latest_map_data = None
        self._obstacle_mask = None

        # Latest known slam_toolbox mode, refreshed from the node itself (see
        # _refresh_slam_mode). None until we have actually heard back.
        self.slam_mode = None

        os.makedirs(
            self.maps_directory,
            exist_ok=True,
        )
        os.makedirs(
            self.paths_directory,
            exist_ok=True,
        )

        # Both topics have to be latched (transient_local): Nav2's
        # KeepoutFilter subscribes to them once, at costmap configure time,
        # and never polls again -- with volatile QoS a filter that comes up
        # after the gateway would sit waiting for a mask that was already
        # sent, and enforce nothing.
        latched = QoSProfile(
            depth=1,
            history=HistoryPolicy.KEEP_LAST,
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
        )

        self.keepout_mask_pub = self.create_publisher(
            OccupancyGrid,
            "/keepout_filter_mask",
            latched,
        )

        self.filter_info_pub = self.create_publisher(
            CostmapFilterInfo,
            "/costmap_filter_info",
            latched,
        )

        self._publish_filter_info()

        threading.Thread(
            target=self._run_ws,
            daemon=True,
        ).start()

        self.cmd_vel_pub = self.create_publisher(
            Twist,
            "/cmd_vel",
            10,
        )

        self.goal_pose_pub = self.create_publisher(
            PoseStamped,
            "/goal_pose",
            10,
        )

        self.serialize_client = self.create_client(
            SerializePoseGraph,
            "/slam_toolbox/serialize_map",
        )

        self.deserialize_client = self.create_client(
            DeserializePoseGraph,
            "/slam_toolbox/deserialize_map",
        )

        # Both slam.launch.py and localization.launch.py name their node
        # "slam_toolbox", so the node name cannot tell mapping from
        # localization. The node's own "mode" parameter can: the mapping config
        # sets online_async, the localization config sets localization.
        self.slam_mode_client = self.create_client(
            GetParameters,
            "/slam_toolbox/get_parameters",
        )

        self.map_sub = self.create_subscription(
            OccupancyGrid,
            "/map",
            self._map_callback,
            10,
        )

        self.odom_sub = self.create_subscription(
            Odometry,
            "/odom",
            self._odom_callback,
            10,
        )

        self.scan_sub = self.create_subscription(
            LaserScan,
            "/scan",
            self._scan_callback,
            10,
        )

        self.create_timer(
            0.1,
            self._publish_cmd_vel,
        )
        self.plan_sub = self.create_subscription(
            Path,
            "/plan",
            self.plan_callback,
            10,
        )
        self.get_logger().info("CommandGatewayNode initialized")
        self._refresh_slam_mode()
        self.create_timer(
            2.0,
            self._refresh_slam_mode,
        )
   

    def plan_callback(self, msg):

        if len(msg.poses) == 0:

            frame = {
                "type": "plan",
                "points": [],
            }

            asyncio.run_coroutine_threadsafe(
                self.websocket_server.broadcast(frame),
                self.websocket_server.loop,
            )

            return

        points = []

        for pose in msg.poses[::5]:

            points.append([
                pose.pose.position.x,
                pose.pose.position.y,
            ])

        frame = {
            "type": "plan",
            "points": points,
        }

        asyncio.run_coroutine_threadsafe(
            self.websocket_server.broadcast(frame),
            self.websocket_server.loop,
        )

        self.get_logger().info(
            f"Broadcasted plan with {len(points)} points"
        )


    def _on_ws_frame(self, data):
       try:

            frame_type = data.get("type")

            if frame_type == "drive":

                self.arbiter.submit_command(
                    source="browser",
                    linear=float(data.get("linear", 0.0)),
                    angular=float(data.get("angular", 0.0)),
                )

            elif frame_type == "nav_goal":

                x = float(data["x"])
                y = float(data["y"])
                theta = float(data["theta"])

                if not (
                    math.isfinite(x)
                    and math.isfinite(y)
                    and math.isfinite(theta)
                ):
                    self.get_logger().warning(
                        "Rejected invalid goal"
                    )
                    return

                goal = PoseStamped()

                goal.header.stamp = self.get_clock().now().to_msg()
                goal.header.frame_id = "map"

                goal.pose.position.x = x
                goal.pose.position.y = y
                goal.pose.position.z = 0.0

                half_theta = theta / 2.0

                goal.pose.orientation.x = 0.0
                goal.pose.orientation.y = 0.0
                goal.pose.orientation.z = math.sin(half_theta)
                goal.pose.orientation.w = math.cos(half_theta)

                self.goal_pose_pub.publish(goal)

                self.get_logger().info(
                    f"Goal published ({x:.2f}, {y:.2f})"
                )


            elif frame_type == "nav_path":

                points = data.get("points", [])

                error = self._validate_path_points(points)

                if error is not None:

                    self.get_logger().warning(
                        f"Rejected nav_path: {error}"
                    )

                    self._broadcast({
                        "type": "path_status",
                        "state": "rejected",
                        "message": error,
                    })

                    return

                # Nav2 would plan around a keep-out on its own, but
                # NavigateThroughPoses treats these points as goal *poses*: a
                # pose inside a zone is simply unreachable, and the run dies
                # partway with an opaque abort. Refusing here names the zone.
                violated = self.zone_store.path_violations(points)

                if violated:

                    message = (
                        "Path crosses keep-out "
                        f"{'zones' if len(violated) > 1 else 'zone'}: "
                        f"{', '.join(violated)}"
                    )

                    self.get_logger().warning(f"Rejected nav_path: {message}")

                    self._broadcast({
                        "type": "path_status",
                        "state": "rejected",
                        "message": message,
                        "zones": violated,
                    })

                    return

                # Same reasoning as the zone check: NavigateThroughPoses
                # treats these as goal poses, and one inside a wall is
                # unreachable, so the run would be accepted and then abort
                # partway with nothing the operator can act on.
                hit = self._path_hits_obstacle(points)

                if hit is not None:

                    message = (
                        "Path runs into an obstacle near "
                        f"({hit[0]:.2f}, {hit[1]:.2f})"
                    )

                    self.get_logger().warning(f"Rejected nav_path: {message}")

                    self._broadcast({
                        "type": "path_status",
                        "state": "rejected",
                        "message": message,
                        "obstacle": [round(hit[0], 3), round(hit[1], 3)],
                    })

                    return

                self.get_logger().info(
                    f"Received nav_path with {len(points)} points"
                )

                self.path_executor.send_path(points)

            elif frame_type == "nav_path_cancel":

                self.path_executor.cancel_path()

            elif frame_type == "zone_list":

                self._broadcast_zones()

            elif frame_type == "zone_save":

                zone_name = self._sanitize_map_name(
                    data.get("name", "")
                )

                if zone_name is None:
                    self._zone_result(False, "Invalid zone name")
                    return

                self._save_zone(
                    zone_name,
                    data.get("polygon", []),
                )

            elif frame_type == "zone_delete":

                zone_name = self._sanitize_map_name(
                    data.get("name", "")
                )

                if zone_name is None:
                    self._zone_result(False, "Invalid zone name")
                    return

                self._delete_zone(zone_name)

            elif frame_type == "zone_clear":

                self._clear_zones()

            elif frame_type == "map_save":

                map_name = self._sanitize_map_name(
                    data.get("name", "")
                )

                if map_name is None:

                    asyncio.run_coroutine_threadsafe(
                        self.websocket_server.broadcast({
                            "type": "map_op_result",
                            "ok": False,
                            "error": "Invalid map name",
                        }),
                        self.websocket_server.loop,
                    )

                    return

                self._save_map(map_name)

            elif frame_type == "map_load":

                map_name = self._sanitize_map_name(
                    data.get("name", "")
                )

                if map_name is None:

                    asyncio.run_coroutine_threadsafe(
                        self.websocket_server.broadcast({
                            "type": "map_op_result",
                            "ok": False,
                            "error": "Invalid map name",
                        }),
                        self.websocket_server.loop,
                    )

                    return

                self._load_map(map_name)
  
            elif frame_type == "map_list":

                self._send_map_list()
            elif frame_type == "path_save":

                path_name = self._sanitize_map_name(
                    data.get("name", "")
                )

                if path_name is None:

                    asyncio.run_coroutine_threadsafe(
                        self.websocket_server.broadcast({
                            "type": "path_op_result",
                            "ok": False,
                            "error": "Invalid path name",
                        }),
                        self.websocket_server.loop,
                    )

                    return

                self._save_path(
                    path_name,
                    data.get("points", []),
                )

            elif frame_type == "path_load":

                path_name = self._sanitize_map_name(
                    data.get("name", "")
                )

                if path_name is None:

                    asyncio.run_coroutine_threadsafe(
                        self.websocket_server.broadcast({
                            "type": "path_op_result",
                            "ok": False,
                            "error": "Invalid path name",
                        }),
                        self.websocket_server.loop,
                    )

                    return

                self._load_path(path_name)

            elif frame_type == "path_list":

                 self._send_path_list()

            elif frame_type == "path_delete":

                path_name = self._sanitize_map_name(
                    data.get("name", "")
                )

                if path_name is None:

                    asyncio.run_coroutine_threadsafe(
                        self.websocket_server.broadcast({
                            "type": "path_op_result",
                            "ok": False,
                            "error": "Invalid path name",
                        }),
                        self.websocket_server.loop,
                    )

                    return

                self._delete_path(path_name)


       except Exception as e:
         self.get_logger().error(f"Map broadcast failed: {e}")
     
    def _broadcast(self, frame):
        """Push a frame to every console, from any thread.

        The websocket thread only publishes .loop once it is up; frames
        produced before that (action feedback, timers, subscriptions) would
        otherwise raise inside whatever callback emitted them.
        """

        if not self.websocket_server.loop:
            return

        asyncio.run_coroutine_threadsafe(
            self.websocket_server.broadcast(frame),
            self.websocket_server.loop,
        )

    def _run_ws(self):
        asyncio.run(self.websocket_server.start())

    
    def _sanitize_map_name(self, name: str):

        if not isinstance(name, str):
            return None

        if not re.fullmatch(
            r"[a-zA-Z0-9_-]+",
            name,
        ):
            return None

        return name
        
        

    # Both the "store this path" and "drive this path" halves have to agree on
    # what a path is, so they share one validator. Returns None when the points
    # are usable, or an operator-facing reason why they are not.
    _MAX_PATH_POINTS = 1000

    def _validate_path_points(self, points):

        if not isinstance(points, list):
            return "Invalid points"

        if len(points) == 0 or len(points) > self._MAX_PATH_POINTS:
            return "Invalid point count"

        for p in points:

            if not isinstance(p, list) or len(p) != 3:
                return "Invalid point format"

            # bool is a subclass of int, and json.dump happily writes NaN and
            # Infinity -- neither of which is valid JSON, and both of which
            # reach Nav2 as an unreachable goal.
            if not all(
                isinstance(v, (int, float))
                and not isinstance(v, bool)
                and math.isfinite(v)
                for v in p
            ):
                return "Invalid point value"

        return None

    def _save_map(self, map_name):

        if not self.serialize_client.service_is_ready():

            asyncio.run_coroutine_threadsafe(
                self.websocket_server.broadcast({
                    "type": "map_op_result",
                    "ok": False,
                    "error": "Serialize service unavailable",
                }),
                self.websocket_server.loop,
            )

            return

        request = SerializePoseGraph.Request()

        request.filename = os.path.join(
            self.maps_directory,
            map_name,
        )

        future = self.serialize_client.call_async(request)

        future.add_done_callback(
            self._save_map_done
        )

    def _save_map_done(self, future):

        try:

            response = future.result()

            # SerializePoseGraph.Response is `uint8 result` with
            # RESULT_SUCCESS = 0 and RESULT_FAILED_TO_WRITE_FILE = 255. Reading
            # it as a truthy value inverts the meaning: a successful save
            # returns 0, which is falsy, so the console showed a failure toast
            # with an empty error string every time a save actually worked.
            ok = (
                response.result
                == SerializePoseGraph.Response.RESULT_SUCCESS
            )

            error = (
                ""
                if ok
                else f"slam_toolbox failed to write the map (result={response.result})"
            )

        except Exception as e:

            ok = False
            error = str(e)

        asyncio.run_coroutine_threadsafe(

            self.websocket_server.broadcast({

                "type": "map_op_result",

                "ok": ok,

                "error": error,

            }),

            self.websocket_server.loop,

        )
    def _load_map(self, map_name):

        if not self.deserialize_client.service_is_ready():

            asyncio.run_coroutine_threadsafe(
                self.websocket_server.broadcast({
                    "type": "map_op_result",
                    "ok": False,
                    "error": "Deserialize service unavailable",
                }),
                self.websocket_server.loop,
            )

            return

        map_path = os.path.join(
            self.maps_directory,
            map_name,
        )

        if not os.path.exists(map_path + ".posegraph"):

            asyncio.run_coroutine_threadsafe(

                self.websocket_server.broadcast({

                    "type": "map_op_result",

                    "ok": False,

                    "error": "Map does not exist",

                }),

                self.websocket_server.loop,

            )

            return

        request = DeserializePoseGraph.Request()

        request.filename = os.path.join(
            self.maps_directory,
            map_name,
        )

        # match_type defaults to UNSET(0), which makes the deserialize a no-op:
        # the pose graph loads but the robot is never placed on it, so "Load"
        # appeared to succeed and changed nothing. START_AT_FIRST_NODE is the
        # right choice for reloading a map in mapping mode; localization mode
        # would want LOCALIZE_AT_POSE with an initial_pose.
        request.match_type = (
            DeserializePoseGraph.Request.START_AT_FIRST_NODE
        )

        future = self.deserialize_client.call_async(request)

        future.add_done_callback(
            self._load_map_done
        )

    def _load_map_done(self, future):

        try:

            # Unlike SerializePoseGraph, DeserializePoseGraph.Response carries
            # no fields at all -- slam_toolbox gives us no success/failure code
            # for a load. So the only failure we can actually observe is the
            # call itself raising. (The pre-flight existence check in _load_map
            # is what catches the common "no such map" case.)
            future.result()

            ok = True
            error = ""

        except Exception as e:

            ok = False
            error = str(e)

        asyncio.run_coroutine_threadsafe(

            self.websocket_server.broadcast({

                "type": "map_op_result",

                "ok": ok,

                "error": error,

            }),

            self.websocket_server.loop,

        )

    def _send_map_list(self):

        try:

            maps = []

            for filename in os.listdir(self.maps_directory):

                if filename.endswith(".posegraph"):

                    maps.append(
                        filename[:-10]
                    )

            maps.sort()

            frame = {

                "type": "map_list",

                "maps": maps,

            }

        except Exception as e:

            frame = {

                "type": "map_op_result",

                "ok": False,

                "error": str(e),

            }

        asyncio.run_coroutine_threadsafe(

            self.websocket_server.broadcast(frame),

            self.websocket_server.loop,

        )
    def _save_path(self, name, points):

        error = self._validate_path_points(points)

        if error is not None:
            self._path_error(error)
            return

        filepath = os.path.join(
            self.paths_directory,
            name + ".json"
        )

        with open(filepath, "w") as f:

            json.dump(
                {
                    "points": points
                },
                f
            )

        asyncio.run_coroutine_threadsafe(
            self.websocket_server.broadcast({
                "type": "path_op_result",
                "ok": True,
                "error": "",
            }),
            self.websocket_server.loop,
        )


    def _load_path(self, name):

        filepath = os.path.join(
            self.paths_directory,
            name + ".json"
        )


        if not os.path.exists(filepath):

            self._path_error(
                "Path does not exist"
            )

            return


        with open(filepath) as f:

            data=json.load(f)


        asyncio.run_coroutine_threadsafe(
            self.websocket_server.broadcast({
                "type":"path_data",
                "name":name,
                "points":data["points"],
            }),
            self.websocket_server.loop,
        )



    def _send_path_list(self):

        try:

            paths=[]

            for file in os.listdir(
                self.paths_directory
            ):

                if file.endswith(".json"):

                    paths.append(
                        file[:-5]
                    )


            paths.sort()


            frame={
                "type":"path_list",
                "paths":paths,
            }


        except Exception as e:

            frame={
                "type":"path_op_result",
                "ok":False,
                "error":str(e),
            }


        asyncio.run_coroutine_threadsafe(
            self.websocket_server.broadcast(frame),
            self.websocket_server.loop,
        )



    def _delete_path(self,name):

        filepath=os.path.join(
            self.paths_directory,
            name+".json"
        )


        if os.path.exists(filepath):

            os.remove(filepath)

            asyncio.run_coroutine_threadsafe(
                self.websocket_server.broadcast({
                    "type":"path_op_result",
                    "ok":True,
                    "error":"",
                }),
                self.websocket_server.loop,
            )

        else:

            self._path_error(
                "Path does not exist"
            )



    def _path_error(self,msg):

        asyncio.run_coroutine_threadsafe(
            self.websocket_server.broadcast({
                "type":"path_op_result",
                "ok":False,
                "error":msg,
            }),
            self.websocket_server.loop,
        )
    # ---- keep-out zones -------------------------------------------------

    def _publish_filter_info(self):
        """Tell KeepoutFilter how to read the mask. Latched, so send once.

        `space = data * multiplier + base`, and the keep-out filter treats the
        result as a cost. Mask cells are 100 (blocked) or 0, which with
        multiplier 1.0 / base 0.0 is the conversion nav2's own keep-out
        tutorial uses.
        """

        info = CostmapFilterInfo()

        info.header.frame_id = "map"
        info.header.stamp = self.get_clock().now().to_msg()

        info.type = 0  # keepout/lanes filter
        info.filter_mask_topic = "/keepout_filter_mask"
        info.base = 0.0
        info.multiplier = 1.0

        self.filter_info_pub.publish(info)

    def _publish_zone_mask(self):
        """Rasterise the stored zones onto the current map grid and publish.

        Silently does nothing until a /map has arrived: the mask has to share
        the map's geometry, and there is nothing to align to before then. The
        map callback calls this again once one shows up.
        """

        map_info = self._latest_map_info

        if map_info is None:
            return

        try:

            data = keepout_zones.rasterise(
                self.zone_store.polygons(),
                map_info.width,
                map_info.height,
                map_info.resolution,
                map_info.origin.position.x,
                map_info.origin.position.y,
                margin_m=self.zone_margin,
            )

        except Exception as e:

            self.get_logger().error(f"Keep-out mask rasterise failed: {e}")
            return

        mask = OccupancyGrid()

        mask.header.frame_id = "map"
        mask.header.stamp = self.get_clock().now().to_msg()

        mask.info = map_info
        mask.data = data

        self.keepout_mask_pub.publish(mask)

        self.get_logger().info(
            f"Published keep-out mask "
            f"({len(self.zone_store.names())} zones, "
            f"margin {self.zone_margin:.2f} m)"
        )

    # ---- obstacles ------------------------------------------------------

    def _ensure_obstacle_mask(self):
        """Build the inflated obstacle mask if the map has changed."""

        if self._obstacle_mask is not None:
            return self._obstacle_mask

        if self._latest_map_info is None or self._latest_map_data is None:
            return None

        info = self._latest_map_info

        try:
            self._obstacle_mask = keepout_zones.inflate_occupancy(
                self._latest_map_data,
                info.width,
                info.height,
                info.resolution,
                self.obstacle_margin,
            )
        except Exception as e:
            self.get_logger().error(f"Obstacle mask build failed: {e}")
            return None

        return self._obstacle_mask

    def _path_hits_obstacle(self, points):
        """First world point where the path runs into a wall, else None.

        Sampled along each segment rather than at the waypoints: the operator
        draws a thinned path, so two legal waypoints can sit either side of a
        wall with the straight line between them going through it.
        """

        mask = self._ensure_obstacle_mask()

        if mask is None:
            # No map yet. Nav2 cannot plan without one either, so let the
            # path through and let the planner produce the real complaint.
            return None

        info = self._latest_map_info

        resolution = info.resolution
        origin_x = info.origin.position.x
        origin_y = info.origin.position.y

        def blocked(x, y):

            col = int((x - origin_x) / resolution)
            row = int((y - origin_y) / resolution)

            if col < 0 or col >= info.width:
                return False
            if row < 0 or row >= info.height:
                return False

            return mask[row * info.width + col] == 1

        # Half a cell, so no sample can step over a one-cell wall.
        step = resolution / 2.0

        for i in range(len(points)):

            x0, y0 = points[i][0], points[i][1]

            if blocked(x0, y0):
                return (x0, y0)

            if i + 1 >= len(points):
                break

            x1, y1 = points[i + 1][0], points[i + 1][1]

            length = math.hypot(x1 - x0, y1 - y0)

            for s in range(1, int(length / step) + 1):

                t = (s * step) / length

                x = x0 + (x1 - x0) * t
                y = y0 + (y1 - y0) * t

                if blocked(x, y):
                    return (x, y)

        return None

    def _broadcast_zones(self):

        self._broadcast({
            "type": "zone_list",
            "zones": self.zone_store.as_list(),
        })

    def _zone_result(self, ok, error=""):

        self._broadcast({
            "type": "zone_op_result",
            "ok": ok,
            "error": error,
        })

    def _save_zone(self, name, polygon):

        error = self.zone_store.add(name, polygon)

        if error is not None:
            self._zone_result(False, error)
            return

        self.get_logger().info(
            f"Saved keep-out zone '{name}' ({len(polygon)} points)"
        )

        self._publish_zone_mask()
        self._zone_result(True)
        self._broadcast_zones()

    def _delete_zone(self, name):

        error = self.zone_store.delete(name)

        if error is not None:
            self._zone_result(False, error)
            return

        self.get_logger().info(f"Deleted keep-out zone '{name}'")

        self._publish_zone_mask()
        self._zone_result(True)
        self._broadcast_zones()

    def _clear_zones(self):

        self.zone_store.clear()

        self.get_logger().warning("Cleared every keep-out zone")

        self._publish_zone_mask()
        self._zone_result(True)
        self._broadcast_zones()

    def _odom_callback(self, msg):

      pose = msg.pose.pose

      q = pose.orientation

      siny_cosp = 2.0 * (
            q.w * q.z +
            q.x * q.y
        )

      cosy_cosp = 1.0 - 2.0 * (
            q.y * q.y +
            q.z * q.z
        )

      yaw = math.atan2(
            siny_cosp,
            cosy_cosp
        )

      self._latest_pose = {
            "x": pose.position.x,
            "y": pose.position.y,
            "yaw": yaw,
        }



    @staticmethod
    def _map_geometry(info):

        if info is None:
            return None

        return (
            info.width,
            info.height,
            info.resolution,
            info.origin.position.x,
            info.origin.position.y,
        )

    def _map_callback(self, msg):

        # Deliberately ahead of the websocket guard below: the keep-out mask
        # has to track the map's geometry whether or not a console is
        # connected. A growing SLAM map re-origins itself as it explores, and
        # a mask still aligned to the old grid would put the no-go areas in
        # the wrong place.
        previous = self._map_geometry(self._latest_map_info)

        self._latest_map_info = msg.info
        self._latest_map_data = msg.data

        # Every map update invalidates the inflated obstacle mask; it is
        # rebuilt on the next path check rather than here.
        self._obstacle_mask = None

        if previous != self._map_geometry(msg.info):
            self._publish_zone_mask()

        # The websocket thread sets .loop once it is up. Maps can arrive
        # before that, and run_coroutine_threadsafe(None) raises inside a
        # subscription callback, so gate on it.
        if not self.websocket_server.loop:
            return

        try:

            frame = encode_occupancy_grid(msg)
            frame["type"] = "map"
            frame["pose"] = self._latest_pose

            asyncio.run_coroutine_threadsafe(
                self.websocket_server.broadcast(frame),
                self.websocket_server.loop,
            )

        except Exception as e:

            self.get_logger().error(
                f"Map broadcast failed: {e}"
            )

    # slam_toolbox's "mode" parameter -> what the operator should see.
    _SLAM_MODE_LABELS = {
        "online_async": "Mapping",
        "online_sync": "Mapping",
        "mapping": "Mapping",
        "localization": "Localization",
    }

    def _refresh_slam_mode(self):
        """Ask slam_toolbox what mode it is in, then broadcast the answer.

        This used to be a hardcoded parameter that nothing ever set, so the
        console read "Mapping" permanently -- including when no SLAM node was
        running at all.
        """

        if not self.slam_mode_client.service_is_ready():
            # No slam_toolbox up (or not up yet). Say so rather than claiming
            # a mode we cannot observe.
            self.slam_mode = None
            self._broadcast_slam_mode()
            return

        request = GetParameters.Request()
        request.names = ["mode"]

        future = self.slam_mode_client.call_async(request)
        future.add_done_callback(self._slam_mode_done)

    def _slam_mode_done(self, future):

        try:
            response = future.result()

            if response.values:
                self.slam_mode = response.values[0].string_value or None
            else:
                self.slam_mode = None

        except Exception as e:
            self.get_logger().warning(
                f"Could not read slam_toolbox mode: {e}"
            )
            self.slam_mode = None

        self._broadcast_slam_mode()

    def _broadcast_slam_mode(self):

        # Fires on a ROS timer that starts before the websocket thread has
        # published its loop; same guard as _map_callback.
        if not self.websocket_server.loop:
            return

        if self.slam_mode is None:
            mode = "Unknown"
        else:
            mode = self._SLAM_MODE_LABELS.get(
                self.slam_mode,
                self.slam_mode.capitalize(),
            )

        frame = {
            "type": "slam_mode",
            "mode": mode,
        }

        asyncio.run_coroutine_threadsafe(
            self.websocket_server.broadcast(frame),
            self.websocket_server.loop,
        )
    

    # A lidar that has gone quiet for longer than this is treated as failed.
    _SCAN_TIMEOUT_SEC = 1.0

    def _scan_callback(self, msg):
        self._latest_scan = msg

    def _closest_in_sector(self, centre_rad, half_width_rad):
        """Nearest valid scan return within a sector, or None.

        The sector is measured in the scan's own frame. The lidar is mounted
        forward of base_link, so this is an approximation of the distance from
        the robot -- deliberately the conservative direction for a forward
        stop, and the stop distance below is set with that in mind.
        """

        scan = self._latest_scan

        if scan is None:
            return None

        closest = None

        for i, distance in enumerate(scan.ranges):

            # inf/NaN mean "nothing seen", and returns outside the sensor's
            # rated band are noise, not obstacles.
            if not math.isfinite(distance):
                continue

            if distance < scan.range_min or distance > scan.range_max:
                continue

            angle = scan.angle_min + i * scan.angle_increment

            # Wrap into [-pi, pi] before comparing, so a sector spanning the
            # 0/2pi seam is not silently empty.
            delta = math.atan2(
                math.sin(angle - centre_rad),
                math.cos(angle - centre_rad),
            )

            if abs(delta) > half_width_rad:
                continue

            if closest is None or distance < closest:
                closest = distance

        return closest

    def _scan_age(self):
        """Seconds since the last scan, or None if none has ever arrived."""

        if self._latest_scan is None:
            return None

        return (
            self.get_clock().now()
            - Time.from_msg(self._latest_scan.header.stamp)
        ).nanoseconds / 1e9

    def _collision_block(self, linear):
        """Reason the requested motion is unsafe, or None if it is fine.

        Only translation is gated. Turning on the spot is how an operator
        gets *out* of a corner, so blocking it would trap the robot against
        whatever it just drove into.
        """

        if abs(linear) < 1e-3:
            return None

        if self.collision_stop_distance <= 0.0:
            return None

        age = self._scan_age()

        # No scan has *ever* arrived: there is no lidar on this robot (or it
        # was never started), and refusing to drive would make teleop useless
        # on a bench rig. Allow it -- the operator is looking at the robot.
        #
        # But a scan that arrived and then stopped is a sensor fault, and
        # driving on the last thing a dead lidar happened to see is exactly
        # the case this guard exists to prevent. Refuse that one.
        if age is not None and age > self._SCAN_TIMEOUT_SEC:
            return (
                f"Lidar stale ({age:.1f} s since last scan) -- "
                f"drive blocked"
            )

        # Forward travel looks ahead; reverse looks behind.
        centre = 0.0 if linear > 0 else math.pi

        closest = self._closest_in_sector(
            centre,
            self.collision_sector_rad / 2.0,
        )

        if closest is None:
            return None

        if closest >= self.collision_stop_distance:
            return None

        direction = "ahead" if linear > 0 else "behind"

        return (
            f"Obstacle {closest:.2f} m {direction} -- "
            f"drive blocked below {self.collision_stop_distance:.2f} m"
        )

    def _publish_cmd_vel(self):
        linear, angular, last_command_time = self.arbiter.get_active_command()

        if (
            last_command_time is None
            or (time.monotonic() - last_command_time) > 0.5
        ):
            return

        blocked = self._collision_block(linear)

        if blocked is not None:

            # Drop the translation but keep the turn, so the operator can
            # rotate away from what they hit.
            linear = 0.0

            now = time.monotonic()

            if (now - self._last_block_notice) > 1.0:

                self._last_block_notice = now

                self.get_logger().warning(blocked)

                self._broadcast({
                    "type": "drive_blocked",
                    "message": blocked,
                })

        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular

        self.cmd_vel_pub.publish(msg)




def main(args=None):
    rclpy.init(args=args)

    node = CommandGatewayNode()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
