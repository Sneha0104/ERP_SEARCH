from django.contrib import admin
from .models import Supplier


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['supplier_code', 'company_name']


admin.site.register(Supplier, SupplierAdmin)
