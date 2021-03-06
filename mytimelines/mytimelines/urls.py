"""mytimelines URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    url(r'^media/(?P<path>.*)', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^addTimeline/$', addTimeline, name="addTimeline"),
    url(r'^test/$', testview, name="test"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^timelines/$', login_required(TimelineListView.as_view()), name="timeline-list"),
    url(r'^timelines/(?P<slug>[\w-]+)/$', timelineview, name="timeline-detail"),
    url(r'^timelines/(?P<slug>[\w-]+)/(?P<event_slug>[\w-]+)/$', eventview,name="event-detail"),
    url(r'^addEvent/$', addEvent, name="addEvent"),
    url(r'^', homeview, name="home")
]

