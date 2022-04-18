from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.mainapp, name="mainapp"),
    path('sets/', views.sets, name='set'),
    path('filter/', views.ProductListView.as_view(), name='product_filter'),
    path('about/', views.about, name='about'),
    path('leave_a_note/', views.post_create, name='post_create'),
    path('product_create/', views.product_create, name='product_create'),
    path('create_product/', views.product_create, name='product_create'),
    path('create_set/', views.set_create, name='set_create'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)