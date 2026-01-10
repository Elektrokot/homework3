from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('catalog/', views.CatalogView.as_view(), name='catalog'),
    path('orders/', views.OrdersView.as_view(), name='orders'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
]
