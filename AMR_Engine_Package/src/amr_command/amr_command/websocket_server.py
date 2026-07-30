"""Websocket server pushing live telemetry to AMR_Operator_Console/frontend
clients, and receiving operator commands to forward into the ROS2 graph.
"""

import asyncio
import json
import time

import websockets


# The console has no other way of telling a live link from a dead one.
#
# A browser WebSocket fires `onclose` only when the TCP connection is actually
# torn down. A gateway that goes away *without* closing it -- Pi powered off,
# Wi-Fi dropped, robot driven out of range -- leaves the client's socket in
# OPEN until the OS gives up retransmitting, which takes minutes. For all of
# that time the console showed "Connected" next to a robot it could not reach.
#
# The protocol's own ping/pong cannot fix this on the browser side: RFC 6455
# pings are answered by the browser itself and are invisible to JavaScript. So
# the liveness signal has to be an ordinary application frame the page can
# watch arrive, which is what this is.
HEARTBEAT_INTERVAL_SEC = 1.0

# Server-side detection of a console that vanished the same way. Well under
# the library's 20 s default because broadcast() walks the connections in
# sequence, so a dead one holds up everyone else's telemetry until it is
# dropped.
PING_INTERVAL_SEC = 5.0
PING_TIMEOUT_SEC = 5.0


class WebsocketServer:
    def __init__(self, host: str = '0.0.0.0', port: int = 8765,
                 status_provider=None):
        self.host = host
        self.port = port
        self.connections = set()
        self._on_message_cb = None
        self.loop = None

        # Returns a dict merged into every heartbeat, so a console learns the
        # gateway's own state (is ROS still spinning, is the e-stop engaged)
        # without polling for it -- and without this transport layer having to
        # know what any of those fields mean.
        self._status_provider = status_provider

    def _heartbeat_frame(self):

        frame = {
            "type": "heartbeat",
            "ts": time.time(),
        }

        if self._status_provider is not None:

            try:
                frame.update(self._status_provider())
            except Exception:
                # The heartbeat's job is to prove the link is alive. A broken
                # status provider must not be the thing that stops it going
                # out and makes the console declare the robot gone.
                frame["status_error"] = True

        return frame

    async def _handle_client(self, websocket):
        try:
            self.connections.add(websocket)

            # Immediately, rather than up to a heartbeat interval later: a
            # console that has just connected should not have to wait to find
            # out what it is talking to.
            await websocket.send(json.dumps(self._heartbeat_frame()))

            async for message in websocket:

                try:
                    frame = json.loads(message)
                except ValueError:
                    # A single malformed frame used to raise straight out of
                    # this loop and drop the connection, so a bad frame on the
                    # console's side became a disconnect on the operator's.
                    print("Discarded malformed frame:", message[:200])
                    continue

                # Answered here rather than handed to the ROS callback. A ping
                # exists to prove the socket round-trips; routing it through
                # the gateway would make a pong prove more than that, and the
                # console reads it as the narrower claim.
                if frame.get("type") == "ping":

                    await websocket.send(json.dumps({
                        "type": "pong",
                        "ts": frame.get("ts"),
                    }))

                    continue

                print("Received:", frame)

                if self._on_message_cb:
                    self._on_message_cb(frame)

        except websockets.exceptions.ConnectionClosed:
            # Normal: the console navigated away, or the ping timeout above
            # dropped a client that stopped answering.
            pass

        finally:
            self.connections.discard(websocket)

    async def start(self):
        self.loop = asyncio.get_running_loop()

        async with websockets.serve(
            self._handle_client,
            self.host,
            self.port,
            ping_interval=PING_INTERVAL_SEC,
            ping_timeout=PING_TIMEOUT_SEC,
        ):
            # This is the "run forever" of the server; it replaces the bare
            # `await asyncio.Future()` that used to hold the loop open.
            await self._heartbeat_loop()

    async def _heartbeat_loop(self):

        while True:

            await asyncio.sleep(HEARTBEAT_INTERVAL_SEC)

            if not self.connections:
                continue

            await self.broadcast(self._heartbeat_frame())

    async def broadcast(self, message: dict):
        json_message = json.dumps(message)
        for websocket in self.connections.copy():
            try:
                await websocket.send(json_message)
            except Exception:
                self.connections.discard(websocket)


if __name__ == "__main__":
    asyncio.run(WebsocketServer().start())
