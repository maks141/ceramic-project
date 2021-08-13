from django.urls import path
from . import views
from .models import Category

app_name = 'catalog'


urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('category/<str:slug>/', views.category_detail, name='category_detail'),
    path('product/<str:slug>', views.product_detail, name='product_detail'),

]
