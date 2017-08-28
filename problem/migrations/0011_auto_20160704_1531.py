# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-04 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0010_auto_20160618_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problembase',
            name='status',
            field=models.IntegerField(choices=[(0, 'Created'), (1, 'Draft'), (2, 'Submitted'), (3, 'Reviewed'), (4, 'Published'), (5, 'Revised'), (6, 'Lock')], default=0),
        ),
    ]
