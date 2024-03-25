from django.urls import path
from . import views

urlpatterns = [
    path('ver_home/', views.ver_home, name="ver_home"),
    path('inserir_home/', views.inserir_home, name="inserir_home")

]


