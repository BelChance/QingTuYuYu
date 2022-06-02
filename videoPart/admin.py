from django.contrib import admin
from .models import VideoIntro


class VideoIntroAdmin(admin.ModelAdmin):
    list_display = ['description', 'photo', 'video']


admin.site.register(VideoIntro, VideoIntroAdmin)
