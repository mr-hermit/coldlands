# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 04:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160317_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag', models.CharField(max_length=32, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='posttags',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(through='blog.PostTags', to='blog.Tag'),
        ),
    ]
