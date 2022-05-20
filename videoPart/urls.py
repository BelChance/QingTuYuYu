from django.urls import path
from . import views

app_name = 'videoPart'  # 设置应用名

urlpatterns = [
    path('video/', views.video, name='video'),
]
