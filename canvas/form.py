from django import forms
from django.forms import ModelForm
from .models import (
    ParceiroModel,
    AtividadeModel,
    RecursoModel,
    PropostaModel,
    RelModel,
    CanalModel,
    SegmentoModel,
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


class RelForm(ModelForm):
    class Meta:
        model = RelModel
        fields = '__all__'


class CanalForm(ModelForm):
    class Meta:
        model = CanalModel
        fields = '__all__'


class SegmentoForm(ModelForm):
    class Meta:
        model = SegmentoModel
        fields = '__all__'
