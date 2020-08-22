import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class tongsofilter(django_filters.FilterSet):
    star_date = DateFilter(field_name="batdau_name", lookup_expr='gte')
    end_date = DateFilter(field_name="batdau_name", lookup_expr='lte')
    doidung_name = CharFilter(field_name="doidung_name", lookup_expr='icontains')

    class Meta:
        model = themmoi_m
        fields = '__all__'
        exclude = ['doidung_name','ketthuc_name','batdau_name']
