from django.contrib import admin
from .models import Shop, Category, Shop_Detail

admin.site.register([Shop, Category, Shop_Detail])
