from django.shortcuts import render, redirect
from .form import (
    ParceiroForm,
    AtividadeForm,
    RecursoForm,
    PropostaForm,
)
from .models import (
    ParceiroModel,
    AtividadeModel,
    RecursoModel,
    PropostaModel,
)


def canvas_list(request):
    parceiro_list = ParceiroModel.objects.all()
    parceiro_form = ParceiroForm()
    atividade_form = AtividadeForm()
    atividade_list = AtividadeModel.objects.all()
    recurso_list = RecursoModel.objects.all()
    recurso_form = RecursoForm()
    proposta_list = PropostaModel.objects.all()
    proposta_form = PropostaForm()
    return render(request, 'canvas/canvas_list.html', {
        'parceiro_list': parceiro_list,
        'parceiro_form': parceiro_form,
        'atividade_list': atividade_list,
        'atividade_form': atividade_form,
        'recurso_list': recurso_list,
        'recurso_form': recurso_form,
        'proposta_list': proposta_list,
        'proposta_form': proposta_form,
        }
    )


def parceiro_add(request):
    form = ParceiroForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')


def atividade_add(request):
    form = AtividadeForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')


def recurso_add(request):
    form = RecursoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')


def proposta_add(request):
    form = PropostaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')