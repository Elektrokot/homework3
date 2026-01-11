from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from catalog.models import Product, Contact, Category
from .forms import ProductForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_products = Product.objects.all().order_by('-created_at')[:5]
        for product in latest_products:
            print(f"Product: {product.title}, Price: {product.price}, Created: {product.created_at}")
        all_products = Product.objects.all()
        paginator = Paginator(all_products, 6)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context


class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_info'] = Contact.objects.first()
        success_message = None
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            email = self.request.POST.get('email')
            message = self.request.POST.get('message')
            success_message = "Сообщение успешно отправлено!"
        context['success_message'] = success_message
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class CatalogView(ListView):
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'page_obj'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.all().order_by('-created_at')


class CategoryListView(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'categories'

class CategoryDetailView(ListView):
    template_name = 'category_detail.html'
    context_object_name = 'page_obj'
    paginate_by = 6

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Product.objects.filter(category=category).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        context['category'] = category
        return context


class OrdersView(TemplateView):
    template_name = 'orders.html'


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('catalog:home')
