from rest_framework import serializers
from Workspace.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

#Workspace Serializer
class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ('owner', 'title','members')
#Card Serializer
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('Workspace', 'front', 'back', 'last_edit', 'locked')
