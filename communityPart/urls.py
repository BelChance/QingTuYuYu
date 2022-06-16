from xml.etree.ElementInclude import include
from django.urls import path
from . import views

app_name = 'communityPart'  # 设置应用名

urlpatterns = [
    path('community/<str:communityName>/', views.community, name='community'),#社区列表
    path('communityDetail/<int:id>/', views.communityDetail, name='communityDetail'),#社区详情
]
