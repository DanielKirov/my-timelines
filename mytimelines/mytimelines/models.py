from django.db import models
from django.contrib.auth.models import User

class Timeline(models.Model):

    user = models.ForeignKey(User, related_name="users")
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to="icons")
    color = models.CharField(max_length=20)

