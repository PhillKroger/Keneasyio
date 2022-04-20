from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import Http404
from django.shortcuts import redirect, render
from django.shortcuts import render
from profiles.forms import UserLoginForm, UserRegistrationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mainapp.models import Product
from mainapp.models import Post
from django.conf import settings
from django.contrib.auth import authenticate

User = get_user_model()

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, email=email, password=password)
        login(request, user)
        return redirect('/')
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        return render(request, 'users/register_done.html',
                      {'new_user': new_user})
    return render(request, 'users/register.html', {'form': form})


def delete_view(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            qs = User.objects.get(pk=user.pk)
    return redirect('/')


def user_account(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        if request.user.is_admin:
            email = request.user
            user = User.objects.get(email=email)
            products = Product.objects.filter(author=user)
            return render(request, 'users/profile.html', {'user': user, 'products': products})
        else:
            email = request.user
            user = User.objects.get(email=email)
            user_posts = Product.objects.filter(author=user)  # .order_by("-pubdate")
            page = request.GET.get('page', 1)
            paginator = Paginator(user_posts, 20)
            try:
                post_list = paginator.page(page)
            except PageNotAnInteger:
                post_list = paginator.page(1)
            except EmptyPage:
                post_list = paginator.page(paginator.num_pages)
            return render(request, 'users/profile.html', {'user': user, 'user_posts': post_list})


def other_account(request, account_id):
    try:
        user = User.objects.get(id=account_id)
    except:
        raise Http404("Пользователь не найден!")
    return render(request, 'users/other_profile.html', {'user': user})

