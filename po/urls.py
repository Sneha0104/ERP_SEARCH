from django.urls import path
from . import views

urlpatterns = [
    path('', views.poHead, name='po'),
    path('poDetail/', views.poDetail, name='poDetail'),
]
