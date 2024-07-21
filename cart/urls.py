from django.urls import path
from .views import add_to_cart, view_cart, cart_item_plus, cart_item_minus, remove_cart_item

urlpatterns = [
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('cart-item-plus/', cart_item_plus, name='cart_item_plus'),
    path('cart-item-minus/', cart_item_minus, name='cart_item_minus'),
    path('remove-cart-item/', remove_cart_item, name='remove_cart_item'),
]
