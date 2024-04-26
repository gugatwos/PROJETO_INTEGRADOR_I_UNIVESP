from django.shortcuts import render, redirect
from lojistas.models import Estoque
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 

@login_required
def estoque(request):
    try:
        lojista = request.user
        return render(request, 'estoque.html', {'lojista': lojista})
    except Exception as e:
        return redirect('index')
    
def pedidos(request):
    try:
        lojista = request.user
        return render(request, 'pedidos.html', {'lojista': lojista})
    except Exception as e:
        return redirect('index')