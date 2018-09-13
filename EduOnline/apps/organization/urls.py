# -*- coding: utf-8 -*-
__author__ = 'zhiqi'
__date__ = '2018/9/13 16:33'
from django.conf.urls import url

from .views import OrgView, AddUserAskView

urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='org_list'),
]

