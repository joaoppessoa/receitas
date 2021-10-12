from django.shortcuts import render

def cadastro(request):
    return render(request, 'users/cadastro.html')

def login(request):
    return render(request, 'users/login.html')

def dashboard(request):
    pass

def logout(request):
    pass