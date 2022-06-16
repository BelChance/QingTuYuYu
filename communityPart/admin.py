from django.contrib import admin
from .models import Community,CommunityImg

class CommunityImgInline(admin.StackedInline):
    model = CommunityImg
    extra = 1     # 默认显示条目的数量

class CommunityAdmin(admin.ModelAdmin):
    inlines = [CommunityImgInline,]

admin.site.register(Community, CommunityAdmin)