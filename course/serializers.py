
# 导入模型
from django import forms
# django 内部的用户模型
from django.contrib.auth.models import User
# 导入序列号器
from rest_framework import serializers

# 导入模型类
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'introduction', 'teacher', 'price')

# django 用户类

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



# 课程类
class CourseSerializer(serializers.ModelSerializer):
    # teacher 是外键字段、是上面user表，可以设置只读
    teacher = serializers.ReadOnlyField(source='teacher.username')

    class Meta:
        model = Course

        # exclude = ('id',) #除了id字段，一个字段但是后面必须加','
        fields = '__all__'  # 所有字段
        #fields = ('name','introduction','teacher','price')
        depth = 2
# 带超链接的课程表
# class CourseSerializer(serializers.HyperlinkedModelSerializer):
#     teacher = serializers.ReadOnlyField(source='teacher.username')
#     class Meta:
#         model = Course
#         # 可以在settings.py中设置url_field_name:'link',加字段
#         fields = ('id','url','name','introduction','teacher','price','created_at','updated_at')
#         # 设置深度 父子表关联
#         depath = 2



















