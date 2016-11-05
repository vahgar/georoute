# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_location_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoadIssues',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
