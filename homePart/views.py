from django.shortcuts import render

# Create your views here.
# 创建视图处理函数


def home(request):
    return render(request, 'homePart.html')
