"""Websocket server pushing live telemetry to AMR_Operator_Console/frontend
clients, and (later) receiving operator commands to forward into the ROS2 graph.
"""

import asyncio
import json
import websockets

class WebsocketServer:
    def __init__(self, host: str = '0.0.0.0', port: int = 8765):
        self.host = host
        self.port = port
        self.connections = set()
        self._on_message_cb = None
        self.loop = None

    async def _handle_client(self, websocket):
        try:
            self.connections.add(websocket)
            async for message in websocket:
                frame = json.loads(message)
                print("Received:", frame)

                if self._on_message_cb:
                    self._on_message_cb(frame)

        finally:
            self.connections.remove(websocket)

    async def start(self):
        self.loop = asyncio.get_running_loop()
        
        async with websockets.serve(
            self._handle_client,
            self.host,
            self.port
        ):
            await asyncio.Future()
       
    async def broadcast(self, message: dict):
        json_message=json.dumps(message)
        for websocket in self.connections.copy():
            try:
                await websocket.send(json_message)
            except Exception:
                self.connections.remove(websocket)
       
if __name__ == "__main__":
    asyncio.run(WebsocketServer().start())