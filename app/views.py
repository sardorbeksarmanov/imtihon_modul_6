from django.shortcuts import render
from shop.models import Shop, Category, Shop_Detail

def home_view(request):
    shoppes = Shop.objects.all()
    categorys = Category.objects.all()
    shop_details = Shop_Detail.objects.all()
    context = {
        "shoppes": shoppes,
        "categorys": categorys,
        "shop_details": shop_details,
    }
    return render(request, 'index.html', context)

def contact_view(request):
    return render(request, 'contact.html')

def shop_view(request):
    shoppes = Shop.objects.all()
    return render(request, 'shop.html', {'shoppes': shoppes})

def testimonial_view(request):
    return render(request, 'testimonial.html')

def chackout_view(request):
    return render(request, 'chackout.html')

def cart_view(request):
    return render(request, 'cart.html')

def shop_detail_view(request):
    shop_details = Shop_Detail.objects.all()
    return render(request, 'shop_detail.html', {'shop_details': shop_details})
