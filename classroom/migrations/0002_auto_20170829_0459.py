# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 04:59
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examanswers',
            name='answers',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='examanswers',
            name='results',
            field=jsonfield.fields.JSONField(),
        ),
    ]
