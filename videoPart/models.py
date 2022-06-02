from django.db import models

# Create your models here.


class VideoIntro(models.Model):  # 视频简介
    description = models.TextField(
        max_length=500, blank=True, null=True)  # 文字描述
    photo = models.ImageField(upload_to='VideoIntro/',
                              blank=True)             # 图片
    video = models.FileField(upload_to='VideoIntro/',
                             blank=True, null=True)  # 视频
