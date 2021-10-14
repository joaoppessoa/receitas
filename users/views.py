from django.shortcuts import render, redirect
from django.contrib.auth.models import User

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
    return render(request, 'users/login.html')

def dashboard(request):
    pass

def logout(request):
    pass