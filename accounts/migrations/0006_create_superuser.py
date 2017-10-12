# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-23 13:00
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import migrations
from accounts.models import User

def create_superuser(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    User.objects.create_user(username="feya", password="hobox1o1*", email="rbarrios@4geeks.co", is_staff=True, is_superuser=True)




class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0005_auto_20171012_1650'),

    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
