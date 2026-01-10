from django.shortcuts import render, get_object_or_404, redirect
from catalog.models import Product, Contact, Category
from django import forms
from django.core.paginator import Paginator

def home(request):
    latest_products = Product.objects.all().order_by('-created_at')[:5]
    for product in latest_products:
        print(f"Product: {product.title}, Price: {product.price}, Created: {product.created_at}")

    all_products = Product.objects.all().order_by('-created_at')
    paginator = Paginator(all_products, 6)  # 6 товаров на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj})

def contacts(request):
    contact_info = Contact.objects.first()
    success_message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        success_message = "Сообщение успешно отправлено!"

    return render(request, 'contacts.html', {
        'success_message': success_message,
        'contact_info': contact_info
    })

def catalog(request):
    all_products = Product.objects.all().order_by('-created_at')
    paginator = Paginator(all_products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalog.html', {'page_obj': page_obj})

def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})

def orders(request):
    return render(request, 'orders.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'category', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category).order_by('-created_at')
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'category_detail.html', {
        'category': category,
        'page_obj': page_obj
    })