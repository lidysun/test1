# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-15 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doubanmovie',
            name='info',
            field=models.CharField(max_length=10000),
        ),
    ]
