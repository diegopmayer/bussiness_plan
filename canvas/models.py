from django.db import models

class CanvasModel(models.Model):
    recurso = models.CharField(max_length=100, null=True, blank=True)
    proposta = models.CharField(max_length=100, null=True, blank=True)
    relacionamento = models.CharField(max_length=100, null=True, blank=True)
    canal = models.CharField(max_length=100, null=True, blank=True)
    segmento = models.CharField(max_length=100, null=True, blank=True)
    custo = models.CharField(max_length=100, null=True, blank=True)
    receita = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.atividade


class ParceiroModel(models.Model):
    parceiro = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.parceiro


class AtividadeModel(models.Model):
    atividade = models.CharField(max_length=100)


    def __str__(self):
        return self.atividade