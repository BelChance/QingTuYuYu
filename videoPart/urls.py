from django.urls import path
from . import views

app_name = 'videoPart'  # 设置应用名

urlpatterns = [
    path('video/<str:videoName>/', views.video, name='video'),
    path('videoDetail/<int:id>/', views.videoDetail, name='videoDetail'),
]
