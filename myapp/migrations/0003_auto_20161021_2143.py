# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.FileField(upload_to=''),
        ),
    ]
