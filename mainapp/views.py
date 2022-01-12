from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView
from .filters import ProductFilter
from .models import Product


def mainapp(request):
    """
    context = {
        'products': Product.objects.all()
    }
    """
    return render(request, "mainapp/main.html")
# context


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    # queryset = User.objects.filter(name__icontains='Bruno') same as

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Product.objects.filter(name__icontains=query)
        else:
            return Product.objects.all() # or .none() depending on what you want to show

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context


def results_view(request):
    results = []
    # Your search/filtering code here...
    query = request.GET.get('query')
    return render(request, 'products/results.html', {
        'results': results,
        'query': query
    })
"""
def news(request):
    posts = Post.objects.all().order_by('-id')[:5]
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 20)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    return render(request, 'posts/news.html', {'posts': post_list})
"""
