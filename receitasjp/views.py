from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita

def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas' : receitas
    }

    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : receita
    }
    return render(request, 'receita.html', receita_a_exibir)

def busca(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        receita_a_buscar = request.GET['buscar']
        
        if index:
            receitas = receitas.filter(nome_receita__icontains=receita_a_buscar)
        

    receita_a_exibir = {
        'receitas' : receitas
    }

    return render(request, 'index.html', receita_a_exibir)