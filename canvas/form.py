from django import forms
from django.forms import ModelForm
from .models import ParceiroModel, AtividadeModel


class ParceiroForm(ModelForm):
    class Meta:
        model = ParceiroModel
        fields = '__all__'


class AtividadeForm(ModelForm):
    class Meta:
        model = AtividadeModel
        fields = '__all__'
