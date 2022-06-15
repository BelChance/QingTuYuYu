from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import VideoIntro
from .models import VideoImg
from django.core.paginator import Paginator
# Create your views here.


def video(request, videoName):
    submenu = videoName
    if videoName == 'video_skill':
        videoName = '技术视频'
    elif videoName == 'video_attack':
        videoName = '战术视频'

    videoList = VideoIntro.objects.all().filter(
        videoType=videoName).order_by('-publishDate')

    p = Paginator(videoList, 2)
    if p.num_pages <= 1:
        pageData = ''
    else:
        page = int(request.GET.get('page', 1))
        videoList = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:
            right = page_range[page:page+2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page-3) if (page-3) > 0 else 0:page-1]
            right = page_range[page:page+2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        pageData = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page,
        }

    return render(
        request, 'videoList.html', {
            'active_menu': 'video',
            'sub_menu': submenu,
            'videoName': videoName,
            'videoList': videoList,
            'pageData': pageData, })


def videoDetail(request, id):
    videod = get_object_or_404(VideoIntro, id=id)
    videoShow = videod.video
    return render(request, 'videoDetail.html', {
        'active_menu': 'videos',
        'videod': videod,
        'videoShow':videoShow,
    })
