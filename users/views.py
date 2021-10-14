from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def cadastro(request):
    if request.method == 'POST':
        post = request.POST

        if not post['nome'].strip():
            print("Campo Nome está em branco.")
            return redirect('cadastro')
        
        if not post['email'].strip():
            print("Campo E-mail está em branco.")
            return redirect('cadastro')

        if post['password'] != post['password2']:
            print("As senhas não são iguais")
            return redirect('cadastro')
        
        if User.objects.filter(email=post['email']).exists() or User.objects.filter(username=post['nome']).exists():
            print("Este e-mail já está em uso.")
            return redirect('cadastro')
        
        user = User.objects.create_user(
            username=post['nome'], 
            email=post['email'], 
            password=post['password'])
        user.save()

        return redirect('login')
    else:
        return render(request, 'users/cadastro.html')

    #return render(request, 'users/cadastro.html')

def login(request):
    if request.method == 'POST':
        post = request.POST

        if post['email'] == "" or post['senha'] == "":
            print("Erro ao fazer login.")
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
        return render(request, 'users/dashboard.html')
    
    return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('index')