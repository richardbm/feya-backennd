# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-23 13:00
from __future__ import unicode_literals
from django.db import migrations
import os
import json


FOLDER_ROOT = os.path.dirname(os.path.abspath(__file__))
FIELD_DATA_FILE = os.path.join(FOLDER_ROOT, "publications.json")



def load_publications(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    publication_model = apps.get_model("blog", "publication")
    category_model = apps.get_model("blog", "category")
    owner = apps.get_model("accounts", "user")
    json_file = open(FIELD_DATA_FILE).read()
    json_data = json.loads(json_file)
    for json_object in json_data:
        publication = publication_model()
        publication.title = json_object["fields"]["title"]
        publication.text = json_object["fields"]["text"]
        publication.owner = owner.objects.first()
        publication.save()
        category, created = category_model.objects.get_or_create(name="Prédicas")
        publication.categories.add(category)


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0008_auto_20171020_0047'),

    ]

    operations = [
        migrations.RunPython(load_publications),
    ]
