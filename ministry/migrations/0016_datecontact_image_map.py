# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ministry', '0015_auto_20171015_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='datecontact',
            name='image_map',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
