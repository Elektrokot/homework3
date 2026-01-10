from django.shortcuts import render
from catalog.models import Product, Contact

def home(request):
    latest_products = Product.objects.all().order_by('-created_at')[:5]
    for product in latest_products:
        print(f"Product: {product.title}, Price: {product.price}, Created: {product.created_at}")

    return render(request, 'home.html')

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
    return render(request, 'catalog.html')

def category(request):
    return render(request, 'category.html')

def orders(request):
    return render(request, 'orders.html')