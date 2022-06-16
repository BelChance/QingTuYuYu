from django.urls import path
from . import views

app_name = 'contactPart'  # 设置应用名

urlpatterns = [
    path('contact/', views.contact, name='contact'),
]
