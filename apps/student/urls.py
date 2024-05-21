
from django.urls import path,include
from rest_framework.routers import DefaultRouter

# 导入视图
from student import views

router = DefaultRouter()
router.register(prefix='viewsets',viewset=views.StudentViewSet)

urlpatterns = [
    # 1.视图第一种函数式视图
    # path('fbv/list/',views.course_list,name='fbv-list'),
    # path('fbv/detail/<int:pk>/',views.course_detail,name='fbv-detail'),
    #
    # # 2.类视图
    # path('cbv/list/',views.CourseList.as_view(),name='cbv-list'),
    # path('cbv/detail/<int:pk>/',views.CourseDetail.as_view(),name='cbv-detail'),
    #
    # # 3.通用类
    # path('gcbv/list/',views.GCourseList.as_view(),name='gcbv-list'),
    # path('gcbv/detail/<int:pk>/',views.GCourseDetail.as_view(),name='gcbv-detail'),

    path('',include(router.urls)),
]





