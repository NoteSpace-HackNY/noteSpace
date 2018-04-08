from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workspace(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owns")
    title = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name="associated")

    def __str__(self):
        return self.title

class Card(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    front = models.TextField()
    back = models.TextField()
    last_edit = models.DateTimeField()
    locked = models.BooleanField(default=False)

    def __str__(self):
        return self.workspace + " " + self.last_edit
