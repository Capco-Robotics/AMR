import asyncio
import math
import time

from rclpy.action import ActionClient

from amr_msgs.msg import LiftState
from amr_msgs.action import MoveLift


class LiftBridge:

    def __init__(self, node):

        self.node = node

        self.action_client = ActionClient(
            node,
            MoveLift,
            "/lift/move"
        )

        self.current_position = 0.0
        self.target_position = 0.0
        self.moving = False

        self.actuator_current = [0.0, 0.0]

        self.limit_upper = False
        self.limit_lower = False

        self.fault = False
        self.overload = False

        self.active_goal = None

        self.last_broadcast = 0.0


        self.state_sub = node.create_subscription(
            LiftState,
            "/lift/state",
            self._lift_state_callback,
            10
        )


        self.node.get_logger().info(
            "LiftBridge initialized"
        )


    # -----------------------------------------
    # Lift State Subscriber
    # -----------------------------------------

    def _lift_state_callback(self, msg):

        self.current_position = msg.position

        self.limit_upper = msg.limit_upper
        self.limit_lower = msg.limit_lower

        self.actuator_current = list(
            msg.actuator_current
        )

        self.fault = msg.level_fault


        now = time.monotonic()

        # 10 Hz throttle
        if now - self.last_broadcast < 0.1:
            return


        self.last_broadcast = now


        frame = {

            "type": "lift",

            "position":
                self.current_position,

            "target":
                self.target_position,

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



    # -----------------------------------------
    # Websocket command handler
    # -----------------------------------------

    def handle(self, data):

        action = data.get(
            "action"
        )


        allowed = [
            "raise",
            "lower",
            "stop",
            "target"
        ]


        if action not in allowed:

            self.send_error(
                "Invalid lift action"
            )

            return



        if action == "target":

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



        if not self.action_client.server_is_ready():

            self.send_error(
                "Lift action server unavailable"
            )

            return



        if action == "raise":

            target = 1.0


        elif action == "lower":

            target = 0.0


        elif action == "target":

            target = float(
                data["target"]
            )


        elif action == "stop":

            self.cancel_goal()

            return



        self.send_goal(
            target
        )



    # -----------------------------------------
    # Send MoveLift goal
    # -----------------------------------------

    def send_goal(self, target):

        goal = MoveLift.Goal()

        goal.target_position = target


        self.target_position = target


        future = (
            self.action_client
            .send_goal_async(goal)
        )


        future.add_done_callback(
            self.goal_response
        )


    def goal_response(self, future):

        goal_handle = future.result()


        if not goal_handle.accepted:

            self.node.get_logger().warning(
                "Lift goal rejected"
            )

            self.moving = False

            return


        self.active_goal = goal_handle

        self.moving = True



    # -----------------------------------------
    # Stop / cancel
    # -----------------------------------------

    def cancel_goal(self):

        if self.active_goal:

            self.active_goal.cancel_goal_async()


        self.moving = False



    # -----------------------------------------
    # Broadcast helper
    # -----------------------------------------

    def broadcast(self, frame):

        if self.node.websocket_server.loop:

            asyncio.run_coroutine_threadsafe(

                self.node.websocket_server.broadcast(
                    frame
                ),

                self.node.websocket_server.loop

            )



    # -----------------------------------------
    # Error frame
    # -----------------------------------------

    def send_error(self, message):

        frame = {

            "type": "error",

            "source": "lift",

            "message": message

        }


        self.broadcast(frame)
