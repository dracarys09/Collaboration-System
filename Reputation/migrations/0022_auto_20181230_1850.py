# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-30 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reputation', '0021_merge_20181230_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcescore',
            name='downvote_value',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='resourcescore',
            name='publish_value',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='resourcescore',
            name='upvote_value',
            field=models.IntegerField(null=True),
        ),
    ]
