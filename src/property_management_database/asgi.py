"""
ASGI config for property_management_database project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from .routing import (
    http_urlpatterns,
    websocket_urlpatterns,
    channel_urlpatterns,
)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'property_management_database.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(websocket_urlpatterns),
    "channel": channel_urlpatterns,
})
