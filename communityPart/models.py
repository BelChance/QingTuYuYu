from django.db import models
from django.utils import timezone

# Create your models here.
class Community(models.Model):
    COMMUNITY_CHOICES = (
        ('足球新闻&小知识', '足球新闻&小知识'),
        ('足球英语', '足球英语'),
        ('体育相关政策', '体育相关政策'),
        ('健康知识','健康知识')
    )
    title = models.CharField(max_length=50, verbose_name=' 社区标题')
    description = models.TextField(verbose_name='社区详情描述')
    communityType = models.CharField(choices=COMMUNITY_CHOICES,
                                   max_length=50,
                                   verbose_name='社区类型')
    price = models.DecimalField(max_digits=7,
                                decimal_places=1,
                                blank=True,
                                null=True,
                                verbose_name='社区发布量')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='发布时间')
    views = models.PositiveIntegerField('浏览量', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '社区'
        verbose_name_plural = '社区'
        ordering = ('-publishDate', )


class CommunityImg(models.Model):
    community = models.ForeignKey(Community,
                                related_name='communityImgs',
                                verbose_name='社区',
                                on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Community/',
                              blank=True,
                              verbose_name='社区图片')

    class Meta:
        verbose_name = '社区图片'
        verbose_name_plural = '社区图片'
