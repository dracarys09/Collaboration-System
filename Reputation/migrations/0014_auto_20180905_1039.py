# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-05 10:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reputation', '0013_auto_20180904_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityreputaion',
            name='community',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Community.Community'),
        ),
        migrations.AlterField(
            model_name='communityreputaion',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
