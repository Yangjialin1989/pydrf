

from django.conf import settings
# django 信号函数
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import renderer_classes,api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,CreateModelMixin
# 类视图
from rest_framework.views import APIView

from .models import Course
# 导入序列化类
from .serializers import CourseSerializer

# 导入权限
from .permissions import IsOwnerReadOnly

# token
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def generate_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)



# 一、函数式编程视图

@api_view(['GET','POST'])
# 私有认证
@authentication_classes((BasicAuthentication,TokenAuthentication))
# 权限认证
@permission_classes((IsAuthenticated))

#@renderer_classes(['JSONRenderer'])
def course_list(request):
    """
    获取所有课程信息或新增一个课程
    :param request:
    :return:
    """
    if request.method == "GET":
        s = CourseSerializer(instance=Course.objects.all(), many=True)


        return Response(data=s.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        s = CourseSerializer(data=request.data)  # 部分更新用partial=True属性
        if s.is_valid():
            s.save(teacher=request.user)
            return Response(data=s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def course_detail(request,pk):
    """

    :param request:
    :param pk:
    :return:
    instance=course  指的是要序列号哪个实例（course查询到的。）
    data=request.data  前端传递过来的数据
    """
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(data={'msg':'没有此课程信息'},status=status.HTTP_404_NOT_FOUND)
    else:
        # 获取
        if request.method == 'GET':
            s = CourseSerializer(instance=course)
            return  Response(data=s.data,status=status.HTTP_200_OK)
        # 更新
        elif request.method == 'PUT':
            # data前端传递的数据，保存更新到数据库序列号pk查询到的指定数据
            s = CourseSerializer(instance=course,data=request.data)
            if s.is_valid():
                s.save()
                return Response(s.data,status=status.HTTP_200_OK)
        # 删除
        elif request.method == 'DELETE':
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

# 二、类视图
"""

"""
class CourseList(APIView):
    authentication_classes = (BasicAuthentication,TokenAuthentication)
    def get(self,request):
        #查询集
        print(self.request.user,self.request.auth)
        print(type(self.request.user))
        queryset = Course.objects.all()
        # instance是查询集
        s = CourseSerializer(instance=queryset,many=True)

        return Response(s.data,status=status.HTTP_200_OK)

    def post(self,request):
        s = CourseSerializer(data=request.data)
        if s.is_valid():
            s.save(teacher=self.request.user)
            return Response(data=s.data,status=status.HTTP_201_CREATED)
        return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

class CourseDetail(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get_object(pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return

    def get(self, request, pk):
        """
        :param request:
        :param pk:
        :return:
        """
        obj = self.get_object(pk=pk)
        if not obj:
            return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)

        s = CourseSerializer(instance=obj)
        return Response(s.data, status=status.HTTP_200_OK)
    # 更新所有字段
    def put(self, request, pk):
        """
        :param request:
        :param pk:
        :return:
        """
        obj = self.get_object(pk=pk)
        if not obj:
            return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)

        s = CourseSerializer(instance=obj, data=request.data)
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_200_OK)
        return Response(data=s.errors, status=status.HTTP_400_BAD_REQUEST)
       # 更新部分字段
    #def patch(self,request,pk):

    def delete(self, request, pk):
        """
        :param request:
        :param pk:
        :return:
        """
        obj = self.get_object(pk=pk)
        if not obj:
            return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 三、通用类视图

class GCourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class GCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated,IsOwnerReadOnly)

# 四、视图集
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    #permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


















# import json
#
# from django.http import JsonResponse
#
# # 针对post请求，需要一个装饰器，取消csrf的限制、
# from django.views.decorators.csrf import csrf_exempt
# # 方法装饰器
# from django.utils.decorators import method_decorator
#
# from django.views import View
#
#
# # Create your views here.
#
# course_dict = {
#     'name':'课程名称',
#     'introduction':'课程介绍',
#     'price':0.11
# }
# # Django 的方法
# @csrf_exempt
# def course_list(request):
#     if request.method == 'GET':
#         return JsonResponse(course_dict)
#
#     if request.method == 'POST':
#         course = json.loads(request.body.decode('utf-8'))
#         return JsonResponse(course,safe=False)# 如果不是字典类型，要false
#
# # drf CBV 编写接口视图
# @method_decorator(csrf_exempt,name='dispatch')
# class CourseList(View):
#     # 处理get请求
#     def get(self,request):
#         return JsonResponse(course_dict)
#
#
#     def post(self,request):
#         course = json.loads(request.body.decode('utf-8'))
#         return JsonResponse(course,safe=False)# 如果不是字典类型，要false

