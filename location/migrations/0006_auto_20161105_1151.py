# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0005_auto_20161105_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='location',
            name='longitude',
        ),
        migrations.AddField(
            model_name='location',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(default='POINT(0 0)', srid=4326),
        ),
    ]
