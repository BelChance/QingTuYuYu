from django.urls import path
from . import views

app_name = 'newsPart'  # 设置应用名

urlpatterns = [
    path('news/', views.news, name='news'),
]
