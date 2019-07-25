from django.urls import path
from . import views

urlpatterns = [
    path('', views.prHead, name='pr'),
    path('prDetail/', views.prDetail, name='prDetail'),
]
