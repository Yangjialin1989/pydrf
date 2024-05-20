# 实现筛选后台模块
from django_filters.rest_framework import DjangoFilterBackend
# 导入筛选类
from .filter import StudentFilter

#
from rest_framework import generics, viewsets

# 数据模型
from .models import Student

# 分页类
from .pagination import StudentPagination

# 导入序列化类
from .serializers import StudentSerializer

# Create your views here.






class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination
    filter_class = StudentFilter
