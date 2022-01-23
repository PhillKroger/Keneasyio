from django.db import models
from django.contrib.auth.models import User
import uuid


class CategorySeason(models.Model):
    name = models.CharField(max_length=255, verbose_name='category_season_name')
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name


class CategoryClothes(models.Model):
    name = models.CharField(max_length=255, verbose_name='category_clothes_name')
    # need_in_set = models.IntegerField(verbose_name='weight_in_set', null=True, default=0)
    img = models.ImageField(verbose_name='img', upload_to='media/categories', null=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class CategorySize(models.Model):
    name = models.CharField(max_length=255, verbose_name='category_size_name')
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name


class CategoryPrice(models.Model):
    name = models.CharField(max_length=255, verbose_name='category_price_name', null=True)
    price = models.IntegerField(verbose_name='product_price', null=True, default=0)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name


class CategoryImage(models.Model):
    name = models.CharField(max_length=255, verbose_name='category_image_name')
    img = models.ImageField(verbose_name='img', upload_to='media/category_image', null=True)

    def __str__(self):
        return "{}".format(self.name)


class Product(models.Model):

    category_season = models.ForeignKey(
        CategorySeason, verbose_name='category_season', on_delete=models.CASCADE, blank=True, null=True
    )

    category_image = models.ForeignKey(
        CategoryImage, verbose_name='category_Image', on_delete=models.CASCADE, blank=True, null=True
    )

    category_clothes = models.ForeignKey(
        CategoryClothes, verbose_name='category_clothes', on_delete=models.CASCADE, blank=True, null=True
    )

    category_size = models.ForeignKey(
        CategorySize, verbose_name='category_size', on_delete=models.CASCADE, blank=True, null=True
    )

    category_price = models.ForeignKey(
        CategoryPrice, verbose_name='category_price', on_delete=models.CASCADE, blank=True, null=True
    )
    color = models.CharField(max_length=255, verbose_name='color', null=True)
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True, null=True)


    def __str__(self):
        return '{} {} {} {} {}'.format(self.slug, self.category_season, self.category_clothes, self.category_size, self.category_price)

