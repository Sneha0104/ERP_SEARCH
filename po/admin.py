from django.contrib import admin
from .models import PODetail, POHead


class PoAdmin(admin.ModelAdmin):
    list_display = ['po_no', 'po_date', 'approved_date']

admin.site.register(POHead,PoAdmin)
admin.site.register(PODetail)
