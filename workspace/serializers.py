from rest_framework import serializers
from .models import Workspace, Card

#Workspace Serializer
class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ('owner', 'title','members', 'id')
#Card Serializer
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('workspace', 'front', 'back', 'last_edit', 'locked', 'id')
