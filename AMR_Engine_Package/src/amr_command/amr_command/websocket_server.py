"""Websocket server pushing live telemetry to AMR_Operator_Console/frontend
clients, and (later) receiving operator commands to forward into the ROS2 graph.
"""


class WebsocketServer:
    def __init__(self, host: str = '0.0.0.0', port: int = 8765):
        self.host = host
        self.port = port

    async def start(self):
        raise NotImplementedError

    async def broadcast(self, message: dict):
        raise NotImplementedError
