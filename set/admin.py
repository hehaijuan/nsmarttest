from django.contrib import admin
from set.models import Setapp


# Register your models here.
class SetappAdmin(admin.ModelAdmin):
    list_display = ['user','id','platformName','platformVersion','deviceName','udid', 'port','deviceselect']

admin.site.register(Setapp,SetappAdmin)  # 把系统设置模块注册到django admin后台并能显示
