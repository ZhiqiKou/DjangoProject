# -*- coding: utf-8 -*-
__author__ = 'zhiqi'
__date__ = '2018/9/17 9:21'
from django.conf.urls import url
from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),

    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),

    # 课程列表页
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),

    # 课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name='course_comment'),

    # 添加kec评论
    url(r'^add_comment/$', AddCommentsView.as_view(), name='add_comment'),
]