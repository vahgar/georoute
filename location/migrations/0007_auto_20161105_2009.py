# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_auto_20161105_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, default='POINT(77.1025 28.7041)'),
        ),
    ]
