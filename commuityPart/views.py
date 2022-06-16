from django.shortcuts import render

from django.shortcuts import HttpResponse
# Create your views here.
# 创建视图处理函数


def commuity(request):

    html = '<html><body>首页</body></html>'
    return HttpResponse(html)
