from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('category/', views.category, name='category'),
    path('catalog/', views.catalog, name='catalog'),
    path('orders/', views.orders, name='orders'),
]

