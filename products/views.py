from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def smartphones(request):
    phones = Product.objects.all()

    brand = request.GET.get('brand')
    if brand:
        phones = phones.filter(brand=brand)

    memory = request.GET.get('memory')
    if memory:
        try:
            memory_int = int(memory)
            phones = phones.filter(memory=memory_int)
        except ValueError:
            pass

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    try:
        if min_price:
            min_price_val = float(min_price)
        else:
            min_price_val = None
    except ValueError:
        min_price_val = None

    try:
        if max_price:
            max_price_val = float(max_price)
        else:
            max_price_val = None
    except ValueError:
        max_price_val = None

    if min_price_val is not None and max_price_val is not None:
        phones = phones.filter(price__gte=min_price_val, price__lte=max_price_val)
    elif min_price_val is not None:
        phones = phones.filter(price__gte=min_price_val)
    elif max_price_val is not None:
        phones = phones.filter(price__lte=max_price_val)

    return render(request, 'products/smartphones.html', {'phones': phones})

def add_to_cart(request, phone_id):
    phone = get_object_or_404(Product, id=phone_id)
    cart = request.session.get('cart', {})

    cart[str(phone_id)] = cart.get(str(phone_id), 0) + 1

    request.session['cart'] = cart

    if request.GET.get('action') == 'proceed_to_cart':
        return redirect('cart_view')
    else:
        phones = Product.objects.all()
        return render(request, 'products/smartphones.html', {
            'phones': phones,
            'message': "Товар добавлен в корзину. Хотите продолжить покупки или перейти в корзину?",
            'last_added_id': phone.id
        })

def support(request):
    return render(request, 'support.html')

def about(request):
    return render(request, 'about.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})
