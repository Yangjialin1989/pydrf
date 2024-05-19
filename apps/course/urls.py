
from django.urls import path,include
from rest_framework.routers import DefaultRouter

# 导入视图
from course import views

router = DefaultRouter()
router.register(prefix='viewsets',viewset=views.CourseViewSet)

urlpatterns = [
    # 1.视图第一种函数式视图
    path('fbv/list/',views.course_list,name='fbv-list'),
    path('fbv/detail/<int:pk>/',views.course_detail,name='fbv-detail'),

    # 2.类视图
    path('cbv/list/',views.CourseList.as_view(),name='cbv-list'),
    path('cbv/detail/<int:pk>/',views.CourseDetail.as_view(),name='cbv-detail'),

    # 3.通用类
    path('gcbv/list/',views.GCourseList.as_view(),name='gcbv-list'),
    path('gcbv/detail/<int:pk>/',views.GCourseDetail.as_view(),name='gcbv-detail'),

    # 4.视图集
    # 4.1 传统
    # path('viewsets/',views.CourseViewSet.as_view(
    #     # {http方法  视图集方法}
    #     {'get':'list','post':'create'}
    # ),name='viewsets-list'),
    # path('viewsets/<int:pk>/',views.CourseViewSet.as_view(
    #     {'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}
    # ),name='viewsets-detail'
    # ),
    path('',include(router.urls))
]





