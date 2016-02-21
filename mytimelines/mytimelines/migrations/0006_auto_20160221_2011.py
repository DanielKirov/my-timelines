# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytimelines', '0005_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpicture',
            name='event',
            field=models.ForeignKey(related_name='pictures', to='mytimelines.Event'),
        ),
    ]
