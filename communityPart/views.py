from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import Community
# Create your views here.
# 创建视图处理函数

def community(request, communityName):
    submenu = communityName
    if communityName == 'knowledge':
        communityName = '足球新闻&小知识'
    elif communityName == 'English':
        communityName = '足球英语'
    elif communityName == 'policy':
        communityName = '体育相关政策'
    else:
        communityName = '健康知识' 

    communityList=Community.objects.all().filter(
        communityType=communityName).order_by('-publishDate')

    p = Paginator(communityList, 2)
    if p.num_pages <= 1:
        pageData = ''
    else:
        page = int(request.GET.get('page', 1))
        communityList = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:
            right = page_range[page:page + 2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            right = page_range[page:page + 2]
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
        request,'communityList.html',{
            'active_menu':'community',
            'sub_menu':submenu,
            'communityName':communityName,
            'communityList':communityList,
            'pageDate':pageData,
        })

def communityDetail(request, id):
    community = get_object_or_404(community, id=id)
    community.views += 1
    community.save()
    return render(request, 'communityDetail.html', {
        'active_menu': 'community',
        'community': community,
    })


