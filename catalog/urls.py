from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('category/', views.category, name='category'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('catalog/', views.catalog, name='catalog'),
    path('orders/', views.orders, name='orders'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
]

