from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contacts(request):
    success_message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        success_message = "Сообщение успешно отправлено!"
    return render(request, 'contacts.html', {'success_message': success_message})

def catalog(request):
    return render(request, 'catalog.html')

def category(request):
    return render(request, 'category.html')

def orders(request):
    return render(request, 'orders.html')