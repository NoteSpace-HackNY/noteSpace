from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack


application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # Put paths here
        ])
    ),
})
