from django.urls import (
    path,
)

from channels.routing import URLRouter, ChannelNameRouter
from property_management_database.app.webrtc.routers import (
    http_urlpatterns as webrtc_http_urlpatterns,
    websocket_urlpatterns as ws_urlpatterns,
)

http_urlpatterns = URLRouter([
    path("", webrtc_http_urlpatterns)
])

websocket_urlpatterns = URLRouter([
    path("", ws_urlpatterns)
])


channel_urlpatterns = ChannelNameRouter({

})