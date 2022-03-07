from django.db import models
from django.contrib.auth.models import User
import uuid
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.conf import settings


class CategorySeason(models.Model):
    name = models.CharField(max_length=255, verbose_name='category_season_name')
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name


class CategoryClothes(models.Model):
    name = models.CharField(max_length=255, verbose_name='category_clothes_name')
    img = models.ImageField(verbose_name='img', upload_to='media/category_image', null=True)
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
    img = models.ImageField(verbose_name='img', upload_to='media/category_image', null=True, blank=True)

    def __str__(self):
        return "{}".format(self.img)


class Product(models.Model):
    img = models.ImageField(verbose_name='img', upload_to='media/', null=True, blank=True)
    category_season = models.ForeignKey(CategorySeason, verbose_name='category_season', on_delete=models.CASCADE, blank=True, null=True)
    category_image = models.ForeignKey(CategoryImage, verbose_name='category_Image', on_delete=models.CASCADE, blank=True, null=True)
    category_clothes = models.ForeignKey(CategoryClothes, verbose_name='category_clothes', on_delete=models.CASCADE, blank=True, null=True)
    category_size = models.ForeignKey(CategorySize, verbose_name='category_size', on_delete=models.CASCADE, blank=True, null=True)
    category_price = models.ForeignKey(CategoryPrice, verbose_name='category_price', on_delete=models.CASCADE, blank=True, null=True)
    color = models.CharField(max_length=255, verbose_name='color', null=True)
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return '{} {} {} {}'.format(self.slug, self.category_season, self.category_clothes, self.category_size)


class Post(models.Model):
    title = models.CharField("phone", max_length=50, null=True)
    email = models.CharField("email", max_length=50, null=True)
    text = RichTextField("Text", null=True)
    file = models.ImageField(verbose_name='verify doc', upload_to='media/docx', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    num = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Set(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', null=True)
    set_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pr = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Set"
        verbose_name_plural = "Sets"