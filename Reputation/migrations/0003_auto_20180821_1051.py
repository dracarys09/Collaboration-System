# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-21 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reputation', '0002_resourcescore_userscore'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourcescore',
            name='can_vote',
        ),
        migrations.AddField(
            model_name='resourcescore',
            name='publish_value',
            field=models.IntegerField(null=True),
        ),
    ]
