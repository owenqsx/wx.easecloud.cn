# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-05 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxauth_router', '0007_auto_20170205_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wechatapp',
            name='domain',
            field=models.CharField(blank=True, help_text='公众号 > 开发 > 接口权限 > 网页授权获取用户基本信息', max_length=100, null=True, verbose_name='公众号网页授权域名'),
        ),
    ]
