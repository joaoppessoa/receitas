from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('receitas/add', views.receita_add, name='receita_add'),
    path('receitas/deletar/<int:receita_id>', views.deletar_receita, name='deletar_receita'),
]