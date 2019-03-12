from django.db import models


class ParceiroModel(models.Model):
    parceiro = models.CharField(max_length=100)


    def __str__(self):
        return self.parceiro


class AtividadeModel(models.Model):
    atividade = models.CharField(max_length=100)


    def __str__(self):
        return self.atividade


class RecursoModel(models.Model):
    recurso = models.CharField(max_length=100)


    def __str__(self):
        return self.recurso


class PropostaModel(models.Model):
    proposta = models.CharField(max_length=100)


    def __str__(self):
        return self.proposta


class RelModel(models.Model):
    relacionamento = models.CharField(max_length=100)


    def __str__(self):
        return self.relacionamento


class CanalModel(models.Model):
    canal = models.CharField(max_length=100)


    def __str__(self):
        return self.canal


class SegmentoModel(models.Model):
    segmento = models.CharField(max_length=100)


    def __str__(self):
        return self.segmento


class CustoModel(models.Model):
    custo = models.CharField(max_length=100)


    def __str__(self):
        return self.custo


class ReceitaModel(models.Model):
    receita = models.CharField(max_length=100)


    def __str__(self):
        return self.receita
