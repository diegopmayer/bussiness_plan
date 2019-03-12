from django.shortcuts import render, redirect
from .form import (
    ParceiroForm,
    AtividadeForm,
    RecursoForm,
    PropostaForm,
    RelForm,
    CanalForm,
    SegmentoForm,
    CustoForm,
)
from .models import (
    ParceiroModel,
    AtividadeModel,
    RecursoModel,
    PropostaModel,
    RelModel,
    CanalModel,
    SegmentoModel,
    CustoModel,
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
    rel_list = RelModel.objects.all()
    rel_form = RelForm()
    canal_list = CanalModel.objects.all()
    canal_form = CanalForm()
    segmento_list = SegmentoModel.objects.all()
    segmento_form = SegmentoForm()
    custo_list = CustoModel.objects.all()
    custo_form = CustoForm()
    return render(request, 'canvas/canvas_list.html', {
        'parceiro_list': parceiro_list,
        'parceiro_form': parceiro_form,
        'atividade_list': atividade_list,
        'atividade_form': atividade_form,
        'recurso_list': recurso_list,
        'recurso_form': recurso_form,
        'proposta_list': proposta_list,
        'proposta_form': proposta_form,
        'rel_list': rel_list,
        'rel_form': rel_form,
        'canal_list': canal_list,
        'canal_form': canal_form,
        'segmento_list': segmento_list,
        'segmento_form': segmento_form,
        'custo_list': custo_list,
        'custo_form': custo_form,
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


def rel_add(request):
    form = RelForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')


def canal_add(request):
    form = CanalForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')


def segmento_add(request):
    form = SegmentoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')


def custo_add(request):
    form  = CustoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')
