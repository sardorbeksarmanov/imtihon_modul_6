from django.urls import path
from .views import home_view, chackout_view, shop_view, testimonial_view, cart_view, contact_view, shop_detail_view
from .views import RegisterView, LoginView, LogoutView


urlpatterns = [
    path('', home_view, name='home'),
    path('chackout/', chackout_view, name='chackout'),
    path('shop/', shop_view, name='shop'),
    path('testimonial/', testimonial_view, name='testimonial'),
    path('cart/', cart_view, name='cart'),
    path('contact/', contact_view, name='contact'),
    path('shop_detail/', shop_detail_view, name='shop_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
