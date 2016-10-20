# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-19 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(blank=True, max_length=120)),
                ('_type', models.CharField(blank=True, choices=[('MC', 'Multiple choice'), ('TB', 'Text-based'), ('TF', 'True or False'), ('MB', 'Map based')], max_length=4, verbose_name='type')),
                ('question', models.TextField(blank=True, verbose_name='question')),
                ('answer', models.TextField(blank=True, verbose_name='right answer')),
                ('answer_type', models.CharField(blank=True, default='ALP', max_length=4, verbose_name='answer type')),
            ],
        ),
    ]
