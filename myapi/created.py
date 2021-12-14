from django_filters import rest_framework as filters
from .models import Driver


class DriverFilter(filters.FilterSet):
    created_at__gte = filters.DateFilter(field_name = 'created_at', lookup_expr = 'gte', input_formats = ["%d-%m-%Y"])
    created_at__lte = filters.DateFilter(field_name = 'created_at', lookup_expr = 'lte', input_formats = ["%d-%m-%Y"])

    class Meta:
        model = Driver
        fields = ['created_at__gte', 'created_at__lte']
