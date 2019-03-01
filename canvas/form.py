from django import forms

class CanvasForm(forms.Form):
    parceiro = forms.CharField()
    atividade = forms.CharField()
    recurso = forms.CharField()
    proposta = forms.CharField()
    relacionamento = forms.CharField()
    canal = forms.CharField()
    segmento = forms.CharField()
    custo = forms.CharField()
    receita = forms.CharField()