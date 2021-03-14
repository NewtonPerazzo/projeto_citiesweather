from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Cidade')
    pais = models.CharField(max_length=100, verbose_name='País')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
