from django.db import models
from django.contrib.auth.models import User

class Timeline(models.Model):

    user = models.ForeignKey(User, related_name="users")
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to="icons")
    color = models.CharField(max_length=20)



class Event(models.Model):

    timeline = models.ForeignKey(Timeline, related_name="events")
    title = models.CharField(max_length=200, null=False, blank=False)
    date = models.DateField()
    main_image = models.ImageField(upload_to="events")



class EventPicture(models.Model):

    event = models.ForeignKey(Event)
    image = models.ImageField(upload_to="events")

