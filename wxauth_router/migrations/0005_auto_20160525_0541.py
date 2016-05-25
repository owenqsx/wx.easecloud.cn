# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 05:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wxauth_router', '0004_auto_20160525_0452'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=32, verbose_name='令牌值')),
                ('expires', models.IntegerField(verbose_name='超时时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='wxauth_router.WechatUser', verbose_name='用户')),
            ],
            options={
                'verbose_name': '结果令牌',
            },
        ),
        migrations.AddField(
            model_name='wechatdomain',
            name='app_secret',
            field=models.CharField(default='', max_length=50, verbose_name='公众号 APP_SECRET'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='authlog',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='wxauth_router.RequestTarget', verbose_name='目标'),
        ),
    ]
