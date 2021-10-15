from django.db import models
from datetime  import datetime
from django.contrib.auth.models import User

class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    redimento = models.TextField(max_length=100)
    categoria = models.CharField(max_length=100)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_receita