from django.contrib import admin
from .models import VideoIntro
from .models import VideoImg


class VideoIntroAdmin(admin.ModelAdmin):
    list_display = ['description', 'photo', 'video']


admin.site.register(VideoIntro)
admin.site.register(VideoImg)
