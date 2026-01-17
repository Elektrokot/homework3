from django.urls import path
from django.views.decorators.cache import cache_page

from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('catalog/', views.CatalogView.as_view(), name='catalog'),
    path('orders/', views.OrdersView.as_view(), name='orders'),
    path('product/<int:pk>/', cache_page(60)(views.ProductDetailView.as_view()), name='product_detail'),
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:category_id>/products/', views.ProductsByCategoryView.as_view(), name='products_by_category'),
]
