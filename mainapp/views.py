from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product


def mainapp(request):

    context = {
        'products': Product.objects.all()
    }
    return render(request, "mainapp/main.html", context)

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