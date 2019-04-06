from django.db import models

# Create your models here.
from django.db import models
class Appcase(models.Model):
    appcasescrip = models.CharField('用例名称',max_length=200)
    appcasename = models.CharField('脚本名称',max_length=200)
    appcaseselect = models.BooleanField('是否选中')
    create_time = models.DateTimeField('创建时间',auto_now=True)

    class Meta:
        verbose_name = 'APP测试用例'
        verbose_name_plural = 'APP测试用例'
    def __str__(self):
        return self.appcasescrip
