# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-16 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_auto_20160916_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_type',
            field=models.CharField(blank=True, default='ALP', max_length=4, null=True, verbose_name='answer type'),
        ),
    ]
