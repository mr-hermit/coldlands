# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-19 01:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160318_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posttags',
            name='post',
        ),
        migrations.RemoveField(
            model_name='posttags',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='PostTags',
        ),
    ]