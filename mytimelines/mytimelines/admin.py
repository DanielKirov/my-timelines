from django.contrib import admin
from .models import Timeline, Event, EventPicture

class TimelineAdmin(admin.ModelAdmin):
    pass

admin.site.register(Timeline, TimelineAdmin)

class EventPictureInline(admin.TabularInline):
    model = EventPicture

class EventAdmin(admin.ModelAdmin):
    inlines = [
        EventPictureInline,
    ]

admin.site.register(Event, EventAdmin)


