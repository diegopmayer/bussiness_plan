from django.db import models

class CanvasModel(models.Model):
    parceiro = models.CharField(max_length=100)
    atividade = models.CharField(max_length=100)
    recurso = models.CharField(max_length=100)
    proposta = models.CharField(max_length=100)
    relacionamento = models.CharField(max_length=100)
    canal = models.CharField(max_length=100)
    segmento = models.CharField(max_length=100)
    custo = models.CharField(max_length=100)
    receita = models.CharField(max_length=100)

    def __str__(self):
        return self.parceiro