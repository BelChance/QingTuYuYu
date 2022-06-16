from django.db import models
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone

# Create your models here.


class MyNew(models.Model):
    NEWS_CHOICES = (
        ('管理团队', '管理团队'),
        ('师资团队', '师资团队'),
        ('课程研发团队', '课程研发团队'),
    )
    title = models.CharField(max_length=50, verbose_name=' 新闻标题')
    description = UEditorField(u'内容',
                               default='',
                               width=1000,
                               height=300,
                               imagePath='news/images/',
                               filePath='news/files/')
    newType = models.CharField(choices=NEWS_CHOICES,
                               max_length=50,
                               verbose_name='新闻类型')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='发布时间')
    views = models.PositiveIntegerField('浏览量', default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishDate']
        verbose_name = "新闻"
        verbose_name_plural = verbose_name
