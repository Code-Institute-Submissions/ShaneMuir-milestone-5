# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-05 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
