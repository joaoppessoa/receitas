from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitasjp.models import Receita

def cadastro(request):
    if request.method == 'POST':
        post = request.POST

        if campo_vazio(post['nome']):
            messages.error(request, "Campo Nome está em branco.")
            return redirect('cadastro')
        
        if campo_vazio(post['email']):
            messages.error(request, "Campo E-mail está em branco.")
            return redirect('cadastro')

        if post['password'] != post['password2']:
            messages.error(request, "As senhas não são iguais.")
            return redirect('cadastro')
        
        if User.objects.filter(email=post['email']).exists():
            messages.error(request, "Este e-mail já está em uso.")
            return redirect('cadastro')
        
        if User.objects.filter(username=post['nome']).exists():
            messages.error(request, "Usuário já cadastrado.")
            return redirect('cadastro')
        
        user = User.objects.create_user(
            username=post['nome'], 
            email=post['email'], 
            password=post['password'])
        user.save()
        messages.success(request, "Usuário cadastrado com sucesso.")

        return redirect('login')
    else:
        return render(request, 'users/cadastro.html')

    #return render(request, 'users/cadastro.html')

def login(request):
    if request.method == 'POST':
        post = request.POST

        if campo_vazio(post['email']) or campo_vazio(post['senha']):
            messages.error(request, "Erro ao fazer login.")
            return redirect('login')
        
        if User.objects.filter(email=post['email']).exists():
            nome = User.objects.filter(email=post['email']).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=post['senha'])

            if user is not None:
                auth.login(request, user)
                print("Login realizado com sucesso.") 

                return redirect('dashboard')

    return render(request, 'users/login.html')

def dashboard(request):
    if request.user.is_authenticated:
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=request.user.id)
        
        dados = { "receitas":receitas }

        return render(request, 'users/dashboard.html', dados)
    
    return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('index')

def receita_add(request):
    if request.method == 'POST':
        post = request.POST
        img_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)

        receita = Receita.objects.create(
            nome_receita=post['nome_receita'],
            ingredientes=post['ingredientes'],
            modo_preparo=post['modo_preparo'],
            tempo_preparo=post['tempo_preparo'],
            redimento=post['rendimento'],
            categoria=post['categoria'],
            pessoa=user,
            foto_receita=img_receita)
        receita.save()

        return redirect('dashboard')
        
    return render(request, 'users/receitas_add.html')

def campo_vazio(campo):
    return not campo.strip()