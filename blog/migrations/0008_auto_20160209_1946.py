# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160205_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
