from django.contrib import admin
from .models import CategorySeason, CategoryClothes, CategorySize, CategoryPrice, Product
#  CategoryColor,
# CategoryGender,
admin.site.register(CategorySeason)
admin.site.register(CategoryClothes)
# admin.site.register(CategoryColor)
admin.site.register(CategorySize)
# admin.site.register(CategoryGender)
admin.site.register(CategoryPrice)
admin.site.register(Product)
