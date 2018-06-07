# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0002_auto_20180605_0831'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvote', models.PositiveIntegerField(default=1)),
                ('downvote', models.PositiveIntegerField(default=1)),
                ('published_author', models.PositiveIntegerField()),
                ('published_publisher', models.PositiveIntegerField()),
                ('comment_flag', models.PositiveIntegerField()),
                ('reply', models.PositiveIntegerField()),
                ('crep_for_art', models.PositiveIntegerField()),
                ('srep_for_art', models.PositiveIntegerField()),
                ('srep_for_comm', models.PositiveIntegerField()),
                ('srep_for_comm_creation', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='systemrep',
            name='sysrep',
            field=models.IntegerField(default=100),
        ),
    ]
