from django.contrib import admin

# Register your models here.

from .models import Course
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # 显示的字段
    list_display = ('name','introduction','teacher','price')

    # 可以搜索的字段
    search_fields = list_display

    # 过滤的字段
    list_filter = list_display

