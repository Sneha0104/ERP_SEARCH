from django.contrib import admin
from .models import InvoiceDetail, InvoiceHead

# Register your models here.


admin.site.register(InvoiceHead)
admin.site.register(InvoiceDetail)
