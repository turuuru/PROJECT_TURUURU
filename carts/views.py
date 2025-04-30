from django.shortcuts import render, get_object_or_404, redirect
from .models import CartItem
from django.contrib.auth.decorators import login_required
from products.models import Product

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart_view')

@login_required
def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    return redirect('cart_view')
