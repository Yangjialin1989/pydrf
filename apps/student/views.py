from rest_framework import generics, viewsets
from .models import Student
# 导入序列化类
from .serializers import StudentSerializer
# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer