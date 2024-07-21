from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from shop.models import Shop
from django.http import JsonResponse


def add_to_cart(request, product_id):
    product = get_object_or_404(Shop, id=product_id)
    cart_item, created = Cart.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('shop')


def view_cart(request):
    cart_items = Cart.objects.all()
    total_price = sum([item.total_price for item in cart_items])
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def cart_item_plus(request):
    item_id = request.GET.get('id')
    cart_item = get_object_or_404(Cart, id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return JsonResponse({'status': 'ok'})


def cart_item_minus(request):
    item_id = request.GET.get('id')
    cart_item = get_object_or_404(Cart, id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return JsonResponse({'status': 'ok'})


def remove_cart_item(request):
    item_id = request.GET.get('id')
    cart_item = get_object_or_404(Cart, id=item_id)
    cart_item.delete()
    return JsonResponse({'status': 'ok'})
