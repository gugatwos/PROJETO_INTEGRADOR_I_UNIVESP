
from django.shortcuts import render
from django.http import HttpResponse

def ver_home(request):
    nome = 'Wash'
    return render(request,'ver_home.html', {'nome':nome})

def inserir_home(request):
    return HttpResponse('Aqui você pode realizar seus pedidos')