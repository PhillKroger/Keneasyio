from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.mainapp, name="mainapp"),
    path('', views.ProductListView.as_view(), name='index'),
    # path('<int:product_id>/', views.detail, name='detail'),
]