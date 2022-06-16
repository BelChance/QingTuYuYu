from django.urls import path
from . import views

app_name = 'newsPart'  # 设置应用名

urlpatterns = [
    path('news/<str:newName>/', views.news, name='news'),
    path('newsDetail/<int:id>/',views.newDetail,name='newDetail'),
    path('search/',views.search,name='search'),
    #path('company/', views.company, name='company'), #企业要闻
    #path('industry/', views.industry, name='industry'),  #行业新闻
    #path('notice/', views.notice, name='notice'),      #通知公告
    #path('com_new/', views.com_new, name='com_new'),      #综合新闻
    #path('spe_new/', views.spe_new, name='spe_new'),      #专题新闻
    #path('man_new/', views.man_new, name='man_new'),      #风云人物
]
