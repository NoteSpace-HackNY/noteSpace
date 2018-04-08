from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import detail_route

from  .models import Workspace, Card
from .serializers import WorkspaceSerializer, CardSerializer

# Create your views here.
class WorkspaceViewset(viewsets.ModelViewSet):
    '''
        API Viewset to retrieve, update, create, and delete Workspace information
    '''
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer

class CardViewset(viewsets.ModelViewSet):
    '''
        API Viewset to retrieve, update, create, and delete Card information
    '''
    queryset = Card.objects.all()
    serializer_class = CardSerializer
