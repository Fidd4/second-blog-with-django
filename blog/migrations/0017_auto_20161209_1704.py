# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20161208_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]