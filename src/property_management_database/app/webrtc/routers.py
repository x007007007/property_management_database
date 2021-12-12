from channels.routing import URLRouter
from django.urls import (
    path,
    re_path,
    include,
)
from .consumer.server_send import (
    ServerSentEventsConsumer,
    BasicHttpConsumer,
    LongPollConsumer,
    AsyncHttpConsumer,
)
from .consumer.ws import EchoConsumer

websocket_urlpatterns = URLRouter([
    path("ws/", EchoConsumer.as_asgi())
])

http_urlpatterns = URLRouter([
    path("server/response/", BasicHttpConsumer.as_asgi()),
    path("server/send/", ServerSentEventsConsumer.as_asgi()),
    path("server/long_poll/", LongPollConsumer.as_asgi()),
    path("server/http/", AsyncHttpConsumer.as_asgi()),
    path("server/event/", AsyncHttpConsumer.as_asgi()),
])