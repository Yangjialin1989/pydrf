from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
#from rest_framework import views
from images import views
router = DefaultRouter()
#router.register(r'files', FileViewset, basename='files')
router.register(prefix='files',viewset=views.FileViewset)
urlpatterns = [
    re_path('^', include(router.urls))
]