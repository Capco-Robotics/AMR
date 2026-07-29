import asyncio
import math
import time

from rclpy.action import ActionClient

from amr_msgs.msg import LiftState
from amr_msgs.action import MoveLift


class LiftBridge:
    """
    Lift ROS <-> WebSocket bridge.

    Responsibilities:
    - Subscribe /lift/state
    - Encode lift telemetry frame
    - Broadcast lift frame through gateway websocket
    - Handle lift_cmd from operator console
    - Send MoveLift action goals
    - Cancel active goals on stop
    """


    def __init__(self, node):

        self.node = node

        # -----------------------------
        # Lift Action Client
        # -----------------------------

        self.action_client = ActionClient(
            node,
            MoveLift,
            "/lift/move"
        )


        # -----------------------------
        # Lift State Cache
        # -----------------------------

        self.position = 0.0
        self.target = 0.0

        self.moving = False

        self.actuator_current = [
            0.0,
            0.0
        ]

        self.limit_upper = False
        self.limit_lower = False

        self.overload = False
        self.fault = False


        self.active_goal = None


        # 10 Hz broadcast throttle

        self.last_broadcast_time = 0.0



        # -----------------------------
        # ROS Subscription
        # -----------------------------

        self.state_sub = node.create_subscription(
            LiftState,
            "/lift/state",
            self._lift_state_callback,
            10
        )


        self.node.get_logger().info(
            "LiftBridge started"
        )



    # =================================================
    # Lift State Callback
    # =================================================

    def _lift_state_callback(self, msg):

        self.position = msg.position

        self.limit_upper = msg.limit_upper
        self.limit_lower = msg.limit_lower

        self.actuator_current = list(
            msg.actuator_current
        )

        self.fault = msg.level_fault


        # overload ticket not available yet

        self.overload = False



        now = time.monotonic()


        # throttle 10Hz

        if (
            now -
            self.last_broadcast_time
        ) < 0.1:

            return


        self.last_broadcast_time = now



        frame = {

            "type": "lift",

            "position":
                self.position,

            "target":
                self.target,

            "moving":
                self.moving,

            "current":
                self.actuator_current,

            "limit_upper":
                self.limit_upper,

            "limit_lower":
                self.limit_lower,

            "overload":
                self.overload,

            "fault":
                self.fault,

        }


        self.broadcast(frame)



    # =================================================
    # Receive websocket lift_cmd
    # =================================================

    def handle(self, data):

        action = data.get(
            "action"
        )


        allowed_actions = {
            "raise",
            "lower",
            "stop",
            "target"
        }


        if action not in allowed_actions:

            self.send_error(
                "Invalid lift action"
            )

            return



        target = None



        if action == "raise":

            target = 1.0



        elif action == "lower":

            target = 0.0



        elif action == "target":

            target = data.get(
                "target"
            )


            if (

                target is None

                or not isinstance(
                    target,
                    (int, float)
                )

                or not math.isfinite(
                    target
                )

                or target < 0.0

                or target > 1.0

            ):

                self.send_error(
                    "Invalid lift target"
                )

                return



        elif action == "stop":

            self.cancel_goal()

            return



        # Non blocking check

        if not self.action_client.server_is_ready():

            self.send_error(
                "Lift action server unavailable"
            )

            return



        self.send_goal(
            float(target)
        )



    # =================================================
    # Send MoveLift Goal
    # =================================================

    def send_goal(self, target):

        goal = MoveLift.Goal()


        goal.target_position = target


        self.target = target


        future = (
            self.action_client
            .send_goal_async(goal)
        )


        future.add_done_callback(
            self._goal_response_callback
        )



    def _goal_response_callback(self, future):

        goal_handle = future.result()


        if not goal_handle.accepted:

            self.node.get_logger().warning(
                "Lift goal rejected"
            )

            self.moving = False

            return



        self.active_goal = goal_handle

        self.moving = True


        self.node.get_logger().info(
            "Lift goal accepted"
        )


        result_future = (
            goal_handle
            .get_result_async()
        )


        result_future.add_done_callback(
            self._goal_finished_callback
        )



    def _goal_finished_callback(self, future):

        self.moving = False

        self.active_goal = None



    # =================================================
    # Cancel Goal
    # =================================================

    def cancel_goal(self):

        if self.active_goal:

            self.active_goal.cancel_goal_async()


        self.moving = False



    # =================================================
    # Websocket Broadcast
    # =================================================

    def broadcast(self, frame):

        if not self.node.websocket_server.loop:

            return



        asyncio.run_coroutine_threadsafe(

            self.node.websocket_server.broadcast(
                frame
            ),

            self.node.websocket_server.loop

        )



    # =================================================
    # Error Frame
    # =================================================

    def send_error(self, message):

        frame = {

            "type": "error",

            "source": "lift",

            "message": message

        }


        self.broadcast(frame)