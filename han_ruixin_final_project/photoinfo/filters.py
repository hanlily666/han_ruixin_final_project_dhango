import django_filters
from .models import *


class PhotoFilter(django_filters.FilterSet):
    class Meta:
        model = Filter
        fields = "__all__"

