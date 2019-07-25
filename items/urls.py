from django.urls import path
from . import views

urlpatterns = [
    path('', views.item, name='item'),
    path('itemDetail/', views.itemDetail, name='itemDetail'),
]
