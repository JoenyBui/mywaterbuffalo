# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 03:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Math',
            fields=[
                ('problembase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problem.ProblemBase')),
                ('qtype', models.IntegerField(choices=[(0, b'Unassigned'), (1, b'Fill in the Blank'), (2, b'True or False'), (3, b'Multiple Choice'), (4, b'Problem Set'), (5, b'Short Answer'), (6, b'Multiple Answer'), (7, b'Word Problem')], default=0)),
                ('stem', django_mysql.models.JSONField(default=dict)),
                ('keys', django_mysql.models.JSONField(default=dict)),
            ],
            bases=('problem.problembase', models.Model),
        ),
        migrations.CreateModel(
            name='Addition',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('mathematics.math',),
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('mathematics.math',),
        ),
        migrations.CreateModel(
            name='Fraction',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('mathematics.math',),
        ),
        migrations.CreateModel(
            name='Multiplication',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('mathematics.math',),
        ),
        migrations.CreateModel(
            name='Subtraction',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('mathematics.math',),
        ),
    ]