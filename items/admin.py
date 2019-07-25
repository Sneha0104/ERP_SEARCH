from django.contrib import admin
from .models import Item, Uom


class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_code', 'item_description', 'uom']


admin.site.register(Item, ItemAdmin)
admin.site.register(Uom)
