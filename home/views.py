from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm


def ver_home(request):
    nome = 'Wash'
    return render(request,'ver_home.html', {'nome':nome})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('nome_da_url_para_pagina_de_pedidos')
        else:
            return render(request, 'home/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'home/login.html', {'form': form})

def inserir_home(request):
    return HttpResponse('Aqui você pode realizar seus pedidos')