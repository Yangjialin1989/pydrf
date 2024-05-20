# 导入模型

# 导入序列号器
from rest_framework import serializers

# 导入模型类
from .models import Student



class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'  # 所有字段
        depth = 2




















