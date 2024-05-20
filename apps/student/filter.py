from django_filters import FilterSet,filters

from .models import Student

class StudentFilter(FilterSet):
    name = filters.CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = Student
        fields = ('name',)

