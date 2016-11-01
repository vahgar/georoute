# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20161101_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(max_digits=8, blank=True, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(max_digits=8, blank=True, decimal_places=5),
        ),
    ]
