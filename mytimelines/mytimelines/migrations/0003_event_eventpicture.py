# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytimelines', '0002_timeline_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('main_image', models.ImageField(upload_to=b'events')),
                ('timeline', models.ForeignKey(related_name='events', to='mytimelines.Timeline')),
            ],
        ),
        migrations.CreateModel(
            name='EventPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'events')),
                ('event', models.ForeignKey(to='mytimelines.Event')),
            ],
        ),
    ]
