# 导入模型

# 导入序列号器
from rest_framework import serializers

# 唯一效验，如果数据库存在某个指定字段会抛出错误。
from rest_framework.validators import UniqueValidator
# 导入模型类
from .models import Student



class StudentSerializer(serializers.ModelSerializer):
    # 注册时候学号sno字段 唯一性效验
    sno = serializers.CharField(
        validators=[UniqueValidator(queryset=Student.objects.all())]
    )

    class Meta:
        model = Student
        fields = '__all__'  # 所有字段
        #fields = ['sno']
        depth = 2




















