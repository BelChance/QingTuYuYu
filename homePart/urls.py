from django.urls import path
from . import views

app_name = 'homePart'  # 设置应用名

urlpatterns = [
    path('', views.home, name='home'),
]
