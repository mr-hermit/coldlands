# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0002_auto_20160305_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navigation.SiteNav'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
