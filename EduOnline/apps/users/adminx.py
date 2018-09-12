# -*- coding: utf-8 -*-
__author__ = 'zhiqi'
__date__ = '2018/9/11 10:54'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner

# xadmin主题配置
class BaseSetting(object):
    # 主题功能
    # 需要使用requests库来替代httplib2
    # 1. 在./xadmin/plugins/themes.py 引入requests
    # 2. 修改block_top_navmenu方法
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'zhiqi Edu 后台管理系统'
    site_footer = 'Zhiqi Edu'
    menu_style = 'accordion'

class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)