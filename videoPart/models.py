from django.db import models
from django.utils import timezone

# Create your models here.


class VideoIntro(models.Model):  # 视频
    VIDEO_CHOICES = (
        ('技术视频', '技术视频'),
        ('战术视频', '战术视频'),
    )
    title = models.CharField(max_length=50, verbose_name='视频标题', default='')
    videoType = models.CharField(
        choices=VIDEO_CHOICES, max_length=50, verbose_name='视频类型', default='技术视频')
    description = models.TextField(
        max_length=500, blank=True, null=True, verbose_name='描述')  # 文字描述
    video = models.FileField(upload_to='VideoIntro/',
                             blank=True, null=True, verbose_name='视频')  # 视频
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='发布时间')

    def __str__(self):
        return self.title
        # 作用：在后台管理系统中以title显示每条数据

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = '视频'
        ordering = ('-publishDate',)


class VideoImg(models.Model):
    video = models.ForeignKey(VideoIntro,
                              related_name='videoImgs', verbose_name='视频', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='VideoIntro/',
                              blank=True, verbose_name='视频封面')

    class Meta:
        verbose_name = '视频封面'
        verbose_name_plural = '视频封面'
