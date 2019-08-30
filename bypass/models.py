from django.db import models

# Create your models here.


class Bypass(models.Model):
    def __str__(self):
        return self.browser_name

    class Meta:
        verbose_name = 'Bypass'
        verbose_name_plural = verbose_name

    browser_name = models.CharField(verbose_name='浏览器名称', max_length=8)
    bot_type = models.CharField(verbose_name='机器人类型', max_length=10, null=True)
    bypass_key = models.CharField(verbose_name='Bypass密匙', max_length=40)
    bypass_status = models.BooleanField(verbose_name='Bypass状态', default=True)
    created = models.DateTimeField(verbose_name='制作时间', auto_now_add=True)


# def get_img_path(instance, filename):  # 指定图片的上传路径
#     return 'item_img{0}/{1}'.format(instance.name, filename)


class Item(models.Model):
    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    item_name = models.CharField(verbose_name='商品名称', max_length=50)
    # item_img = models.ImageField(verbose_name='商品图片', upload_to=get_img_path)
    item_url = models.URLField(verbose_name='商品链接', max_length=90)
    item_variants = models.CharField(verbose_name='库存信息', max_length=200, null=True)
    item_site = models.CharField(verbose_name='商品站名', max_length=10, null=True)
    item_price = models.IntegerField(verbose_name='商品价格')
    item_sku = models.CharField(verbose_name='库存信息', max_length=100, null=True)
    item_update_time = models.DateTimeField(verbose_name='更新时间', auto_now_add=True)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_show = models.BooleanField(verbose_name='上架状态', default=False)


class Task(models.Model):
    def __str__(self):
        return self.task_name

    class Meta:
        verbose_name = '任务'
        verbose_name_plural = verbose_name

    task_name = models.CharField(verbose_name='任务名称', max_length=50)
    bot_name = models.CharField(verbose_name='机器人名', max_length=10, null=True)
    bot_type = models.CharField(verbose_name='机器人类型', max_length=10, null=True)
    task_status = models.IntegerField(verbose_name='任务状态')
    is_on = models.BooleanField(verbose_name='是否开启', default=False)
    task_update_time = models.DateTimeField(verbose_name='更新时间', auto_now_add=True)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)


class BpMission(models.Model):
    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'BP记录'
        verbose_name_plural = verbose_name
    is_on = models.BooleanField(verbose_name='任务状态', default=True)
    bot_name = models.CharField(verbose_name='机器人名', max_length=10, null=True)
    is_success = models.BooleanField(verbose_name='是否成功')
    log = models.CharField(verbose_name='任务', max_length=20)
    created = models.DateTimeField(verbose_name='任务开始时间', auto_created=True)
    updated = models.DateTimeField(verbose_name='任务结束时间')


class Bot(models.Model):
    def __str__(self):
        return self.bot_name

    class Meta:
        verbose_name = 'BOT'
        verbose_name_plural = verbose_name
    bot_name = models.CharField(verbose_name='任务状态', max_length=10)
    bot_type = models.CharField(verbose_name='机器人类型', max_length=10, null=True)
    bot_number = models.IntegerField(verbose_name='Bot编号')
    user_location = models.URLField(verbose_name='用户路径')
    created_time = models.DateTimeField(verbose_name='BOT创建时间', auto_now_add=True)


class FogBot(models.Model):
    def __str__(self):
        return self.bot_name

    class Meta:
        verbose_name = 'FOGBOT'
        verbose_name_plural = verbose_name
    bot_name = models.CharField(verbose_name='任务状态', max_length=10)
    bot_type = models.CharField(verbose_name='机器人类型', max_length=10, null=True)
    bot_number = models.IntegerField(verbose_name='Bot编号')
    user_location = models.URLField(verbose_name='用户路径')
    created_time = models.DateTimeField(verbose_name='BOT创建时间', auto_now_add=True)


class Proxies(models.Model):
    proxy_provider = models.CharField(verbose_name='供应商', max_length=20, null=True)
    proxy_id = models.CharField(verbose_name='代理编号', max_length=3, null=True)
    proxy_ip = models.CharField(verbose_name='代理地址', max_length=20)
    proxy_port = models.IntegerField(verbose_name='代理端口')
    proxy_usr = models.CharField(verbose_name='代理账号', max_length=10, null=True)
    proxy_psw = models.CharField(verbose_name='代理密码', max_length=20, null=True)
    in_use = models.BooleanField(verbose_name='正在使用', default=False, null=True)
    status = models.BooleanField(verbose_name='代理状态', default=True, null=True)
    chrome_id = models.IntegerField(verbose_name='正在使用的chrome编号', null=True)


class AutoBypass(models.Model):
    bp_type = models.CharField(verbose_name='自动BP类型', max_length=20, null=True)
    is_on = models.BooleanField(verbose_name='开启状态', default=False)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now_add=True)
