# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-13 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxauth_router', '0018_auto_20170313_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alipayapp',
            name='app_id',
            field=models.CharField(max_length=176, unique=True, verbose_name='APP_ID'),
        ),
        migrations.AlterField(
            model_name='alipayapp',
            name='app_secret',
            field=models.CharField(blank=True, max_length=255, verbose_name='APP_SECRET'),
        ),
        migrations.AlterField(
            model_name='alipaymapiapp',
            name='app_id',
            field=models.CharField(max_length=176, unique=True, verbose_name='APP_ID'),
        ),
        migrations.AlterField(
            model_name='alipaymapiapp',
            name='app_secret',
            field=models.CharField(blank=True, max_length=255, verbose_name='APP_SECRET'),
        ),
        migrations.AlterField(
            model_name='paypalapp',
            name='app_id',
            field=models.CharField(max_length=176, unique=True, verbose_name='APP_ID'),
        ),
        migrations.AlterField(
            model_name='paypalapp',
            name='app_secret',
            field=models.CharField(blank=True, max_length=255, verbose_name='APP_SECRET'),
        ),
        migrations.AlterField(
            model_name='wechatapp',
            name='app_id',
            field=models.CharField(max_length=176, unique=True, verbose_name='APP_ID'),
        ),
        migrations.AlterField(
            model_name='wechatapp',
            name='app_secret',
            field=models.CharField(blank=True, max_length=255, verbose_name='APP_SECRET'),
        ),
    ]
