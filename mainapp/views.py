from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView
from .filters import ProductFilter
from .models import Product, CategoryPrice
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm
from django.shortcuts import render, redirect
import datetime


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


class CategoryPr:
    def get_prices(self):
        return CategoryPrice.objects.all()


class ProductListView(ListView):

    model = Product
    template_name = 'products/filter.html'
    # queryset = Product.objects.filter(draft=False)

    def get_queryset(self):
        query = self.request.GET.get('search')
        p = Product.objects.all()
        # b = Product.objects.filter().values('category_clothes', 'category_price', 'category_season', 'category_size', 'slug')
        # l = [value for value in b if isinstance(value, dict)]
        # print(l)

        if query:
            pn = Product.objects.filter(name__icontains=query)
            return pn
        else:
            return p

    def get_context_data(self, *, object_list=None, **kwargs):
        c = super().get_context_data(**kwargs)
        c['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return c