# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20171020_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
        migrations.AddField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=None, verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default=None, max_length=200),
        ),
    ]