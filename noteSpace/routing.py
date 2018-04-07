from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import workspace.routing

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # Put paths here
            workspace.routing.websocket_urlpatterns,
        ])
    ),
})
