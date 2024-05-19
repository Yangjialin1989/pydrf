
# 导入模型
from django import forms
# django 内部的用户模型
from django.contrib.auth.models import User
# 导入序列号器
from rest_framework import serializers

# 导入模型类
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'  # 所有字段
        depth = 2




















