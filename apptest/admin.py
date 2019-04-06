from django.contrib import admin
from apptest.models import Appcase

# Register your models here.
class AppcaseAdmin(admin.ModelAdmin):
    list_display = ['appcasescrip','appcasename','appcaseselect','create_time','id']
admin.site.register(Appcase,AppcaseAdmin)