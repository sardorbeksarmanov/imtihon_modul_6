from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Cart


class CartResource(resources.ModelResource):
    class Meta:
        model = Cart


class CartAdmin(ImportExportModelAdmin):
    resource_class = CartResource


admin.site.register(Cart, CartAdmin)
