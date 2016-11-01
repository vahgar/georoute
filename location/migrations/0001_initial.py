# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('point', location_field.models.plain.PlainLocationField(blank=True, max_length=63, null=True)),
                ('description', models.TextField(blank=True)),
                ('problem_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
