# -*- coding: utf-8 -*-
__author__ = 'zhiqi'
__date__ = '2018/9/11 13:15'

import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCourse
from organization.models import CourseOrg

class LessonInLine(object):
    model = Lesson
    extra = 0

class CourseResourceInLine(object):
    model = CourseResource
    extra = 0

class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time', 'get_chapter_num','go_to']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']
    # 按点击数倒序排列
    ordering = ['-click_nums']
    # 把收藏数设为已读
    readonly_fields = ['fav_nums']
    # 点击数设为隐藏
    exclude = ['click_nums']
    # 课程和章节、课程资源组合到同一界面
    inlines = [LessonInLine, CourseResourceInLine]
    # 直接在列表页编辑
    list_editable = ['degree', 'desc']
    # 对列表页进行刷新,从下面列表中选择
    refresh_times = [3, 5]

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs.filter(is_banner=False)

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()



class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']
    # 按点击数倒序排列
    ordering = ['-click_nums']
    # 把收藏数设为已读
    readonly_fields = ['fav_nums']
    # 点击数设为隐藏
    exclude = ['click_nums']
    # 课程和章节、课程资源组合到同一界面
    inlines = [LessonInLine, CourseResourceInLine]

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs.filter(is_banner=True)


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download',  'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)