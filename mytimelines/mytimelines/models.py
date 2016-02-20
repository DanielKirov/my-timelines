from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from utilities.picofyer import thumblyFy, createName
from PIL import Image
from django.core.files.storage import default_storage


class Timeline(models.Model):

    user = models.ForeignKey(User, related_name="users")
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to="icons")
    color = models.CharField(max_length=20,default="")

    def __unicode__(self):
        return self.title

    def oval_icon(self):
        django_image = self.icon
        pillow_image = Image.open(django_image)
        thumblyFy(pillow_image, django_image.url)
        return createName(django_image.url) + '_thumbnail.png'

    def get_absolute_url(self):
        return reverse('timeline-detail', kwargs={"slug": self.pk, })

class Event(models.Model):
    timeline = models.ForeignKey(Timeline, related_name="events")
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=500, default="")
    date = models.DateField()
    main_image = models.ImageField(upload_to="events")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={"slug": self.timeline.pk, "event_slug": self.pk})

class EventPicture(models.Model):

    event = models.ForeignKey(Event)
    image = models.ImageField(upload_to="events")

