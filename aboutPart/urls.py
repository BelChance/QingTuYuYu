from django.urls import path
from . import views

app_name = 'aboutPart'  # 设置应用名

urlpatterns = [
    path('about/', views.about, name='about'),
]
