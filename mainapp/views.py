from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView
from .filters import ProductFilter
from .models import Product


def mainapp(request):
    return render(request, "mainapp/index.html")


def about(request):
    return render(request, 'mainapp/about.html')


class ProductListView(ListView):
    model = Product
    template_name = 'products/filter.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        p = Product.objects.all()

        if query:
            pn = Product.objects.filter(name__icontains=query)
            return pn
        else:
            return p

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context
