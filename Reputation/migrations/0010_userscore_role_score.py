# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-28 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reputation', '0009_auto_20180828_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscore',
            name='role_score',
            field=models.CharField(default='role_score', max_length=20),
        ),
    ]
