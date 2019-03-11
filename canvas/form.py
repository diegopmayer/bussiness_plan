from django import forms
from django.forms import ModelForm
from .models import (
    ParceiroModel,
    AtividadeModel,
    RecursoModel,
    PropostaModel,
)


class ParceiroForm(ModelForm):
    class Meta:
        model = ParceiroModel
        fields = '__all__'


class AtividadeForm(ModelForm):
    class Meta:
        model = AtividadeModel
        fields = '__all__'


class RecursoForm(ModelForm):
    class Meta:
        model = RecursoModel
        fields = '__all__'


class PropostaForm(ModelForm):
    class Meta:
        model = PropostaModel
        fields = '__all__'
