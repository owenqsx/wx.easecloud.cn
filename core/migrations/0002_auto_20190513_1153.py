# Generated by Django 2.2 on 2019-05-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wechatapp',
            name='trade_type',
            field=models.CharField(choices=[('JSAPI', '公众号JSAPI'), ('NATIVE', '扫码支付'), ('APP', 'APP支付'), ('WAP', '网页WAP'), ('MINIAPP', '微信小程序')], max_length=20, verbose_name='支付方式'),
        ),
        migrations.AlterField(
            model_name='wechatapp',
            name='type',
            field=models.CharField(choices=[('APP', '移动应用'), ('NATIVE', '网站应用'), ('BIZ', '公众账号'), ('MINIAPP', '微信小程序')], help_text='参照 http://open.weixin.qq.com 管理中心的应用类型', max_length=20, verbose_name='开放平台类型'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar', verbose_name='头像文件'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='city',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='country',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='国家'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='headimgurl',
            field=models.URLField(blank=True, null=True, verbose_name='用户头像'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='nickname',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='用户昵称'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='privilege',
            field=models.TextField(blank=True, null=True, verbose_name='用户特权信息'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='province',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='省份'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='sex',
            field=models.IntegerField(blank=True, choices=[(0, '未知'), (1, '男'), (2, '女')], null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='unionid',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='用户unionid'),
        ),
    ]