# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('django_th', '0011_digest'),
    ]

    operations = [
        migrations.AddField(
            model_name='triggerservice',
            name='counter_ko',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='triggerservice',
            name='counter_ok',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userservice',
            name='counter_ko',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userservice',
            name='counter_ok',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rss',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='triggerservice',
            name='date_result',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
