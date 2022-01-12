from django.contrib import admin
from .models import CategorySeason, CategoryClothes, CategorySize, CategoryPrice, Product

admin.site.register(CategorySeason)
admin.site.register(CategoryClothes)
admin.site.register(CategorySize)
admin.site.register(CategoryPrice)
admin.site.register(Product)

