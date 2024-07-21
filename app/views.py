from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, hashers, authenticate, login, logout
from django.contrib import messages
from django.views import View
from .forms import RegisterForm, LoginForm
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


User = get_user_model()


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            # first_name = request.POST.get('first_name')
            first_name = form.cleaned_data.get('first_name')
            # last_name = request.POST.get('last_name')
            last_name = form.cleaned_data.get('last_name')
            # email = request.POST.get('email')
            email = form.cleaned_data.get('email')
            # username = request.POST.get('username')
            username = form.cleaned_data.get('username')
            # password1 = request.POST.get('password')
            password1 = form.cleaned_data.get('password')
            # password2 = request.POST.get('password_confirm')
            password2 = form.cleaned_data.get('password_confirm')

            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('/login')
                elif User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists!')
                    return redirect('/login')
                else:
                    user = User.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        username=username,
                        password=hashers.make_password(password1)
                    )
                    user.save()
                    return redirect('/login')
            else:
                messages.error(request, 'Passwords are not same!')
                return redirect('/register')


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Username or password invalid!')
                return redirect('/register')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')