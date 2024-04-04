from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate



def ver_home(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                
                return HttpResponse('você foi logado')
    else:
        form = AuthenticationForm()
    return render(request, 'ver_home.html', {'form': form})

def login(request):
    return HttpResponse('Aqui você pode realizar seus pedidos')

def inserir_home(request):
    return HttpResponse('Aqui você pode realizar seus pedidos')