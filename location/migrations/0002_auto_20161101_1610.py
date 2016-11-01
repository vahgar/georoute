# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='point',
        ),
        migrations.RemoveField(
            model_name='location',
            name='problem_type',
        ),
        migrations.AddField(
            model_name='location',
            name='category',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(blank=True, max_digits=8, default='0.000', decimal_places=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(blank=True, max_digits=8, default='0.000', decimal_places=3),
            preserve_default=False,
        ),
    ]
