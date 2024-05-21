# 实现筛选后台模块
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend

from . import models
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

from rest_framework.decorators import action

# Create your views here.
# 批量删除
from rest_framework import status
from rest_framework.response import Response


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination
    filter_class = StudentFilter
    # 根据sno批量删除
    ordering_fields = ('sno',)
    filterset_fields = ('sno',)

    @action(methods=['DELETE'], detail=False)
    def bulk_destroy(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.filter(sno__in=request.data['snos']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# 导入表单类



