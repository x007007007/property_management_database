import asyncio
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class EchoConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        print(self.scope)

        await self.accept()

    async def disconnect(self, code):
        print(code)

    async def receive(self, text_data):
        """
        Receive message from WebSocket.
        Get the event and send the appropriate event
        """
        response = json.loads(text_data)
        print(text_data)
        event = response.get("event", None)
        message = response.get("message", None)
        print(event)
        print(message)

    async def send_message(self, res):
        """ Receive message from room group """
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "payload": res,
        }))
