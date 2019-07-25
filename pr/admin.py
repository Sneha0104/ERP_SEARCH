from django.contrib import admin
from .models import PRDetail, PRHead


class PrAdmin(admin.ModelAdmin):
    list_display = ['pr_no', 'pr_date', 'approved_date']


admin.site.register(PRHead, PrAdmin)
admin.site.register(PRDetail)
