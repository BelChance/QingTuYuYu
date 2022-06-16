from django.shortcuts import render
from .models import VideoIntro
# Create your views here.


def video(request):
    videos = VideoIntro.objects.all()
    return render(request, 'video.html', {
        'videos': videos
    })
