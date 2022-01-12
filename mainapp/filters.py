import django_filters as filters
from .models import Product


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ('category_season', 'category_size')