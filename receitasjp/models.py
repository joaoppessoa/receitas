from django.db import models
from datetime  import datetime
from pessoas.models import Pessoas

class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    redimento = models.TextField(max_length=100)
    categoria = models.CharField(max_length=100)
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)