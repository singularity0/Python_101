# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=140)),
                ('week', models.IntegerField()),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]
