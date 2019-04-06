
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from set.models import Setapp
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
#设置管理
@login_required
def setapp_manage(request):
    username = request.session.get('user', '')
    set_list = Setapp.objects.all()
    return render(request, "setapp_manage.html", {"user": username, "setapps": set_list})
# 搜索功能
@login_required
def setsearch(request):
     username = request.session.get('user', '') # 读取浏览器登录session
     search_setname = request.GET.get("setname", "")
     set_list = Set.objects.filter(setname__icontains=search_setname)
     return render(request,'setapp_manage.html', {"user": username,"setapps":set_list})
