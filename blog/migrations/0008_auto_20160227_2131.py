# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 02:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160227_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tmppost',
            name='tags',
        ),
        migrations.DeleteModel(
            name='tmpPost',
        ),
        migrations.DeleteModel(
            name='tmpTags',
        ),
    ]
