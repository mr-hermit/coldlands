# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 04:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wsglobal', '0004_auto_20160316_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinfo',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wsglobal.Site', unique=True),
        ),
    ]
