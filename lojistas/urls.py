# lojistas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('redirect_stock/', views.redirect_to_lojista_stock, name='redirect_to_lojista_stock'),
    path('estoque/<int:lojista_id>/', views.estoque_lojista, name='estoque_lojista'),
]
