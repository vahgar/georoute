# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=50, blank=True)),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', blank=True, related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', related_name='user_set', blank=True, related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', accounts.models.NewUserManager()),
            ],
        ),
    ]
