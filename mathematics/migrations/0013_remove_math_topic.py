# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-09 00:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mathematics', '0012_auto_20160721_0241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='math',
            name='topic',
        ),
    ]
