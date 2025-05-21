from django.shortcuts import render, get_object_or_404, redirect
from .models import CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from django.core.mail import send_mail
from django.conf import settings

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        comment = request.POST.get('order_comments', '').strip()
        
        # Отправка письма на почту администратора
        subject = f'Новый заказ от {request.user.username}'
        message = f'Комментарий пользователя: {comment}\n\nСодержимое корзины:\n'
        for item in cart_items:
            message += f'- {item.product.name} x {item.quantity} (Цена: {item.product.price})\n'
        message += f'\nИтоговая сумма: {total_price} KZT'
        
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['roldsi71@gmail.com'])
        
        # Очистка корзины
        cart_items.delete()
        messages.success(request, 'Покупка успешно оформлена! Спасибо за заказ.')
        return redirect('cart_view')

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'Товар {product.name} обновлен в корзине.')
    else:
        messages.success(request, f'Товар {product.name} добавлен в корзину.')
    return redirect('cart_view')

@login_required
def remove_from_cart(request, item_id):
    try:
        item = CartItem.objects.get(id=item_id, user=request.user)
        item.delete()
        messages.success(request, 'Товар удален из корзины.')
    except CartItem.DoesNotExist:
        messages.error(request, 'Товар не найден в корзине.')
    return redirect('cart_view')

@login_required
def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    messages.success(request, 'Корзина очищена.')
    return redirect('cart_view')
