# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscrivers',
            fields=[
                ('mail', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('name', models.TimeField(max_length=50)),
                ('ip', models.TextField(max_length=20)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
