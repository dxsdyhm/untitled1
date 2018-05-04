from django.contrib import admin

# Register your models here.
from wechat import models


@admin.register(models.wxInfo)
class weChatAdmin(admin.ModelAdmin):
    list_display = ('type','frome','text')
    list_filter = ('frome',)