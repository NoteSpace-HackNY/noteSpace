from django.urls import path, include
from rest_framework.routers import DefaultRouter

from workspace.views import WorkspaceViewset, CardViewset
router = DefaultRouter()
router.register('workspace', WorkspaceViewset)
router.register('card', CardViewset)

urlpatterns = [
    path('api/', include(router.urls)),
]
