# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='auth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]
