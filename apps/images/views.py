from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import FilesModel
from .serializer import FilesSerializer


# Create your views here.
class FileViewset(viewsets.ModelViewSet):
    """ 文件上传 """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = FilesModel.objects.all()
    serializer_class = FilesSerializer