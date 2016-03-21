# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('wsglobal', '0001_initial'), ('wsglobal', '0002_siteinfo'), ('wsglobal', '0003_auto_20160315_1532'), ('wsglobal', '0004_auto_20160316_0004'), ('wsglobal', '0005_auto_20160316_0028'), ('wsglobal', '0006_auto_20160316_0041'), ('wsglobal', '0007_remove_siteinfo_link'), ('wsglobal', '0008_auto_20160317_1014'), ('wsglobal', '0009_hitcount'), ('wsglobal', '0010_message')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(blank=True, max_length=255, null=True)),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wsglobal.Site')),
            ],
        ),
        migrations.CreateModel(
            name='HitCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modified')),
                ('url', models.CharField(max_length=200, verbose_name='URL')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='Hits')),
            ],
            options={
                'ordering': ('-created', '-modified'),
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=100)),
                ('sender_email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
            ],
        ),
    ]
