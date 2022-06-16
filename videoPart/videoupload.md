# 作业 
web开发--数据库模型

## 在setting.py中添加代码：存储媒体文件相关的代码。
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

## 在models.py中加入模型
建一个类，里面包含需要上传的文件类型，比如FileField，创建完成输入下面两行代码
python manage.py makemigrations 
python manage.py migrate

## 创建超级管理员 
python manage.py createsuperuser

## 将模型注册到后台系统--编辑同model文件下的admin.py文件
以列表的形式辅助存储

## 在主项目文件夹的urls.py加入代码
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)