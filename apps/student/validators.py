"""
自定义验证器
1.自定义验证器，
2.然后再序列号器中使用
"""
from rest_framework import exceptions
from django.contrib.auth import get_user_model

User = get_user_model()


def validate_username_not_taken(username):
    if User.objects.filter(username=username).exists():
        raise exceptions.ValidationError("该用户名已被占用")






