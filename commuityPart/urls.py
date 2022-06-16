from django.urls import path
from . import views

app_name = 'commuityPart'  # 设置应用名

urlpatterns = [
    path('commuity/', views.commuity, name='commuity'),
]
