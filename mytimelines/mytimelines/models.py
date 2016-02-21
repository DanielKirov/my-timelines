from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from utilities.picofyer import thumblyFy, createName
from PIL import Image
import datetime

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
    description = models.CharField(max_length=500,default="")
    date = models.DateField()
    time = models.TimeField(blank=True,default=datetime.time(0,0))
    main_image = models.ImageField(upload_to="events")


    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={"slug": self.timeline.pk, "event_slug": self.pk})

    @property
    def main_image_binary(self):
        try:
            img = open(self.main_image.path, "rb")
            data = img.read()
            return "data:image/jpg;base64,%s" % data.encode('base64')

        except IOError:
            return self.main_image.url

    def get_json_format(self):
        '{"Event":{ \
            "Time":{ \
                "Date":{ \
                    "Day": 23, \
                    "Month": 7, \
                    "Year": 2012 \
                }, \
                "TimeOfDay":{ \
                    "Hour": 16, \
                    "Minutes": 30, \
                    "Seconds": 40 \
                } \
            }, \
            "Data":{ \
                "Message": "Today was a good damn day", \
                "Name": "My Birthday", \
                "Icon": "76924374uh2l3r7hq23bnr4pd9q78e38g2w3jinr2p" \
            } \
        }}'

        result = {} # Main body
        time_data = {}
        event_data = {}


        # TimeOfDay is optional
        if self.time:
            timeofday_data = dict(
                Hour=int(self.time.hour),
                Minutes=int(self.time.minute),
                Seconds=int(self.time.second)
            )
        else:
            timeofday_data = {}

        date_data = dict(
            Day=int(self.date.day),
            Month=int(self.date.month),
            Year=int(self.date.year)
        )

        time_data['Date'] = date_data
        if timeofday_data:
            time_data['TimeOfDay'] = timeofday_data

        event_data['Time'] = time_data

        data_data = dict(
            Message=self.description,
            Name=self.title,
            Icon=self.main_image_binary
        )

        event_data['Data'] = data_data
        result['Event'] = event_data
        return result

class EventPicture(models.Model):

    event = models.ForeignKey(Event)
    image = models.ImageField(upload_to="events")

