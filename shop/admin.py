from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Shop, Category


class CartResource(resources.ModelResource):
    class Meta:
        model = Shop


class ShopAdmin(ImportExportModelAdmin):
    resource_class = CartResource


admin.site.register(Shop, ShopAdmin)
admin.site.register(Category)
