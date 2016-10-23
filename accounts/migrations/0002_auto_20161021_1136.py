# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, null=True, max_length=128),
        ),
    ]
