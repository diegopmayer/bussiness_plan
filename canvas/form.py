from django import forms

class CanvasForm(forms.Form):
    parceiro = forms.CharField()
    atividade = forms.CharField()
