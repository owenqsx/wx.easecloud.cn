# Generated by Django 2.0.5 on 2018-06-14 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlipayApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='可以填写公众号的显示名称', max_length=150, verbose_name='标题')),
                ('app_id', models.CharField(max_length=176, unique=True, verbose_name='APP_ID')),
                ('app_secret', models.CharField(blank=True, max_length=255, verbose_name='APP_SECRET')),
                ('notify_url', models.URLField(blank=True, default='', verbose_name='授权回调地址')),
                ('return_url', models.URLField(blank=True, default='', verbose_name='授权跳转地址')),
                ('cancel_url', models.URLField(blank=True, default='', verbose_name='取消操作返回 URL')),
                ('oauth_redirect_url', models.URLField(blank=True, default='', help_text='如果是，请务必将本地址设定为本 API 的 index，例如 http://wx.easecloud.cn并且在对应的平台中注册此地址，不填的话默认会使用当前地址', verbose_name='OAuth 认证跳转地址')),
                ('mch_id', models.CharField(blank=True, default='', max_length=50, verbose_name='商户号 MCH ID')),
                ('app_gateway', models.CharField(blank=True, default='', help_text='除服务窗外其他的应用，目前未做强制校验，可以不用填写', max_length=150, verbose_name='应用网关')),
                ('rsa2_app_key_public', models.TextField(blank=True, default='', verbose_name='RSA2(SHA256)应用公钥')),
                ('rsa2_app_key_private', models.TextField(blank=True, default='', verbose_name='RSA2(SHA256)应用私钥')),
                ('rsa2_alipay_key_public', models.TextField(blank=True, default='', verbose_name='RSA2(SHA256)支付宝公钥')),
                ('rsa_app_key_public', models.TextField(blank=True, default='', verbose_name='RSA(SHA1)应用公钥')),
                ('rsa_app_key_private', models.TextField(blank=True, default='', verbose_name='RSA(SHA1)应用私钥')),
                ('rsa_alipay_key_public', models.TextField(blank=True, default='', verbose_name='RSA(SHA1)支付宝公钥')),
                ('aes_key', models.CharField(blank=True, default='', max_length=150, verbose_name='接口AES密钥')),
            ],
            options={
                'verbose_name': '支付宝APP',
                'verbose_name_plural': '支付宝APP',
                'db_table': 'wxauth_alipay_app',
            },
        ),
        migrations.CreateModel(
            name='AlipayMapiApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='可以填写公众号的显示名称', max_length=150, verbose_name='标题')),
                ('app_id', models.CharField(max_length=176, unique=True, verbose_name='APP_ID')),
                ('app_secret', models.CharField(blank=True, max_length=255, verbose_name='APP_SECRET')),
                ('notify_url', models.URLField(blank=True, default='', verbose_name='授权回调地址')),
                ('return_url', models.URLField(blank=True, default='', verbose_name='授权跳转地址')),
                ('cancel_url', models.URLField(blank=True, default='', verbose_name='取消操作返回 URL')),
                ('oauth_redirect_url', models.URLField(blank=True, default='', help_text='如果是，请务必将本地址设定为本 API 的 index，例如 http://wx.easecloud.cn并且在对应的平台中注册此地址，不填的话默认会使用当前地址', verbose_name='OAuth 认证跳转地址')),
                ('seller_email', models.CharField(blank=True, help_text='卖家Email或手机号', max_length=255, verbose_name='卖家支付宝用户号')),
                ('seller_account_name', models.CharField(blank=True, max_length=255, verbose_name='卖家支付宝账号别名')),
            ],
            options={
                'verbose_name': '支付宝旧版APP',
                'verbose_name_plural': '支付宝旧版APP',
                'db_table': 'wxauth_alipay_mapi_app',
            },
        ),
        migrations.CreateModel(
            name='ResultTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=32, verbose_name='令牌值')),
                ('expires', models.IntegerField(verbose_name='超时时间')),
            ],
            options={
                'verbose_name': '结果令牌',
                'db_table': 'wxauth_result_ticket',
            },
        ),
        migrations.CreateModel(
            name='WechatApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='可以填写公众号的显示名称', max_length=150, verbose_name='标题')),
                ('app_id', models.CharField(max_length=176, unique=True, verbose_name='APP_ID')),
                ('app_secret', models.CharField(blank=True, max_length=255, verbose_name='APP_SECRET')),
                ('notify_url', models.URLField(blank=True, default='', verbose_name='授权回调地址')),
                ('return_url', models.URLField(blank=True, default='', verbose_name='授权跳转地址')),
                ('cancel_url', models.URLField(blank=True, default='', verbose_name='取消操作返回 URL')),
                ('oauth_redirect_url', models.URLField(blank=True, default='', help_text='如果是，请务必将本地址设定为本 API 的 index，例如 http://wx.easecloud.cn并且在对应的平台中注册此地址，不填的话默认会使用当前地址', verbose_name='OAuth 认证跳转地址')),
                ('mch_id', models.CharField(blank=True, default='', max_length=50, verbose_name='商户号 MCH ID')),
                ('api_key', models.CharField(blank=True, default='', max_length=50, verbose_name='API 密钥')),
                ('apiclient_cert', models.TextField(blank=True, default='', verbose_name='PEM 支付证书')),
                ('apiclient_key', models.TextField(blank=True, default='', verbose_name='PEM 支付私钥')),
                ('trade_type', models.CharField(choices=[('JSAPI', '公众号JSAPI'), ('NATIVE', '扫码支付'), ('APP', 'APP支付'), ('WAP', '网页WAP')], max_length=20, verbose_name='支付方式')),
                ('type', models.CharField(choices=[('APP', '移动应用'), ('NATIVE', '网站应用'), ('BIZ', '公众账号')], help_text='参照 http://open.weixin.qq.com 管理中心的应用类型', max_length=20, verbose_name='开放平台类型')),
                ('domain', models.CharField(blank=True, help_text='公众号 > 开发 > 接口权限 > 网页授权获取用户基本信息', max_length=100, null=True, verbose_name='公众号网页授权域名')),
                ('verify_key', models.CharField(blank=True, default='', max_length=20, verbose_name='公众平台认证文件编码')),
                ('biz_account', models.CharField(blank=True, default='', max_length=20, verbose_name='公众平台微信号')),
                ('biz_origin', models.CharField(blank=True, default='', max_length=20, verbose_name='公众平台原始ID')),
                ('biz_token', models.CharField(blank=True, default='', max_length=20, verbose_name='公众平台接口令牌')),
                ('biz_aes_key', models.CharField(blank=True, default='', max_length=100, verbose_name='公众平台AES密钥')),
                ('withdraw_app', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='wxapp', to='core.WechatApp', verbose_name='提现关联公众号')),
            ],
            options={
                'verbose_name': '微信APP',
                'verbose_name_plural': '微信APP',
                'db_table': 'wxauth_wechat_app',
            },
        ),
        migrations.CreateModel(
            name='WechatUser',
            fields=[
                ('openid', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='用户OpenID')),
                ('nickname', models.CharField(max_length=128, null=True, verbose_name='用户昵称')),
                ('sex', models.IntegerField(choices=[(0, '未知'), (1, '男'), (2, '女')], null=True, verbose_name='性别')),
                ('province', models.CharField(max_length=120, null=True, verbose_name='省份')),
                ('city', models.CharField(max_length=120, null=True, verbose_name='城市')),
                ('country', models.CharField(max_length=120, null=True, verbose_name='国家')),
                ('headimgurl', models.URLField(null=True, verbose_name='用户头像')),
                ('avatar', models.ImageField(null=True, upload_to='avatar', verbose_name='头像文件')),
                ('privilege', models.TextField(null=True, verbose_name='用户特权信息')),
                ('unionid', models.CharField(max_length=64, null=True, verbose_name='用户unionid')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('app', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='users', to='core.WechatApp', verbose_name='微信APP')),
            ],
            options={
                'verbose_name': '微信用户',
                'verbose_name_plural': '微信用户',
                'db_table': 'wxauth_wechat_user',
                'ordering': ['-date_updated', '-pk'],
            },
        ),
        migrations.CreateModel(
            name='WechatWithdrawTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=32, verbose_name='令牌值')),
                ('expires', models.IntegerField(verbose_name='超时时间')),
                ('amount', models.IntegerField(help_text='单位：分', verbose_name='提现金额')),
                ('status', models.TextField(choices=[('PENDING', '申请中'), ('SUCCESS', '成功'), ('FAIL', '失败'), ('REJECTED', '驳回')], default='PENDING', verbose_name='提现状态')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='withdraw_tickets', to='core.WechatUser', verbose_name='提现用户')),
            ],
            options={
                'verbose_name': '提现票据',
                'db_table': 'wxauth_wechat_withdraw_ticket',
            },
        ),
        migrations.AddField(
            model_name='resultticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='core.WechatUser', verbose_name='用户'),
        ),
    ]