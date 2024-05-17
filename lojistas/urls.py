from django.urls import path
from . import views

urlpatterns = [
    path('estoque/', views.estoque, name='estoque'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('api/estoque/', views.estoque_api, name='api_estoque'),
    path('finalizar-compra/', views.finalizar_compra, name='finalizar_compra'),
    path('atualizar-status/<int:venda_id>/', views.atualizar_status, name='atualizar_status'),
]
