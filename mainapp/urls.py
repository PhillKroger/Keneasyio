from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainapp, name="mainapp"),
    path('filter/', views.ProductListView.as_view(), name='index'),
    # path('results/', views.results_view, name='results'),
]