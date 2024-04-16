from django.contrib import admin
from .models import Produto, Lojista, Estoque, Vendas

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'quantidade')
    search_fields = ('descricao',)

class LojistaAdmin(admin.ModelAdmin):
    list_display = ('user', 'endereco', 'telefone', 'email')
    search_fields = ('user__username', 'endereco')

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade')
    search_fields = ('produto__descricao',)

class VendasAdmin(admin.ModelAdmin):
    list_display = ('processo', 'lojista', 'valor_produto')
    search_fields = ('lojista__user__username',)

# Registro dos modelos com as classes ModelAdmin
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Lojista, LojistaAdmin)
admin.site.register(Estoque, EstoqueAdmin)
admin.site.register(Vendas, VendasAdmin)
