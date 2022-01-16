from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView
from .filters import ProductFilter
from .models import Product


def mainapp(request):
    return render(request, "mainapp/main.html")


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    # queryset = User.objects.filter(name__icontains='Bruno') same as

    def get_queryset(self):
        query = self.request.GET.get('search')
        p = Product.objects.all()
        l = []
        for i in range(len(p)):
            l.append(p[i])

        # Average price across all books.
        # from django.db.models import Avg
        # Book.objects.all().aggregate(Avg('price'))
        # {'price__avg': 34.35}


        """
         a = [10, 20 ,30 ,40 ,50 ,60 ,70 ,80, 90]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        c = [2, 4, 8, 10, 12, 14, 16, 18]
        d = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        f = 35
        k = 0
        for q in range(len(a)-1):
          for w in range(len(b)-1):
            for e in range(len(c)-1):
              for r in range(len(d)-1):
                if (a[q] + b[w] + c[e] + d[r]) <= f:
                  k+= 1
                  print(a[q], b[w], c[e], d[r])
        print(k)
        """


        if query:
            pn = Product.objects.filter(name__icontains=query)
            return pn
        else:
            a = Product.objects.filter(
                category_clothes__need_in_set=4
            )
            b = Product.objects.filter(
                category_clothes__need_in_set=3
            )
            c = Product.objects.filter(
                category_clothes__need_in_set=2
            )
            d = Product.objects.filter(
                category_clothes__need_in_set=1
            )
            return p


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