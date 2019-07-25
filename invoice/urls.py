from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice, name='invoice'),
    path('invoiceDetail', views.invoiceDetail, name='invoiceDetail'),
]
