from django.shortcuts import render
from .models import Product


def phone_list(request):
    phones = Product.objects.all()
    print(phones)  # Выводим список телефонов в консоль
    return render(request, 'products/phone_list.html', {'phones': phones})

def index(request):
    return render(request, 'products/index.html')

def smartphones(request):
    return render(request, 'products/smartphones.html')

def accessories(request):
    return render(request, 'products/accessories.html')

def support(request):
    return render(request, 'products/support.html')

def about(request):
    return render(request, 'products/about.html')
