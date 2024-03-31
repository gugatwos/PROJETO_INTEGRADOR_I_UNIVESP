from django.shortcuts import render, redirect
from lojistas.models import Estoque
from django.contrib.auth.decorators import login_required

@login_required
def redirect_to_lojista_stock(request):
    return redirect('estoque_lojista', lojista_id=request.user.lojista.id)

@login_required
def estoque_lojista(request, lojista_id):
    estoque = Estoque.objects.filter(lojista_id=lojista_id)
    return render(request, 'lojistas/estoque.html', {'estoque': estoque})
