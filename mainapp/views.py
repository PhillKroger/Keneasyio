from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView
from .filters import ProductFilter
from .models import Product, CategoryPrice
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm, ProductForm, SetForm
from django.shortcuts import render, redirect
import datetime
from .models import *


def mainapp(request):
    return render(request, "mainapp/index.html")


def about(request):
    return render(request, 'mainapp/about.html')


def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pubdate = datetime.datetime.now()
            post.save()
            form = PostForm()
            return redirect('/profile/')

    return render(request, 'posts/form.html', {'form': form})


def product_create(request):
    form = ProductForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.pubdate = datetime.datetime.now()
            product.save()
            form = ProductForm()
            return redirect('/profile/')

    return render(request, 'products/form.html', {'form': form})


def set_create(request):
    form = SetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            set = form.save(commit=False)
            set.author = request.user
            set.save()
            form = SetForm()
            return redirect('/profile/')

    return render(request, 'sets/form.html', {'form': form})


def sets(request):
    sets = Set.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(sets, 20)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request, 'products/filter_set.html', {'sets': sets})


class ProductListView(ListView):
    model = Product
    template_name = 'products/filter.html'
    # queryset = Product.objects.filter(draft=False)

    def get_queryset(self):
        query = self.request.GET.get('search')
        p = Product.objects.all()
        # b = Product.objects.filter().values('category_clothes', 'category_price')
        # l = [value for value in b if isinstance(value, dict)]

        if query:
            pn = Product.objects.filter(name__icontains=query)
            return pn
        else:
            return p

    def get_context_data(self, *, object_list=None, **kwargs):
        c = super().get_context_data(**kwargs)
        c['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return c
