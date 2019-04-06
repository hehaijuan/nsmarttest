from django.db import models

# Create your models here.
from django.db import models
class Setapp(models.Model):
    user = models.CharField('用户名',max_length=200)
    platformName = models.CharField('手机平台',max_length=200)
    platformVersion = models.CharField('手机平台版本号',max_length=200)
    deviceName = models.CharField('手机型号',max_length=200)
    udid = models.CharField('手机设备号',max_length=200)
    port = models.IntegerField('端口号')
    deviceselect = models.BooleanField('是否选中')
    create_time = models.DateTimeField('创建时间',auto_now=True)

    class Meta:
        verbose_name = 'APP系统设置'
        verbose_name_plural = 'APP系统设置'
    def __str__(self):
        return self.udid
