from django.shortcuts import render, redirect
from .form import ParceiroForm, AtividadeForm
from .models import ParceiroModel, AtividadeModel


def canvas_list(request):
    parceiro_list = ParceiroModel.objects.all()
    atividade_form = AtividadeForm()
    atividade_list = AtividadeModel.objects.all()
    parceiro_form = ParceiroForm()
    return render(request, 'canvas/canvas_list.html', {
        'parceiro_list': parceiro_list,
        'parceiro_form': parceiro_form,
        'atividade_list': atividade_list,
        'atividade_form': atividade_form,
        }
    )


def parceiro_add(request):
    form = ParceiroForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')


def atividade_add(request):
    atividade = AtividadeForm(request.POST or None)
    if atividade.is_valid():
        atividade.save()

    return redirect('canvas_list')
