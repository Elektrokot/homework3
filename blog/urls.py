from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('list/', views.BlogPostListView.as_view(), name='blog_list'),
    path('/<int:pk>/', views.BlogPostDetailView.as_view(), name='blog_detail'),
    path('create/', views.BlogPostCreateView.as_view(), name='blog_create'),
    path('update/<int:pk>/', views.BlogPostUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>/', views.BlogPostDeleteView.as_view(), name='blog_delete'),
]