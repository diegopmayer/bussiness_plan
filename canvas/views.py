from django.shortcuts import render, redirect
from .form import ParceiroForm, AtividadeForm
from .models import ParceiroModel, AtividadeModel


def canvas_list(request):
    list_canvas_model = ParceiroModel.objects.all()
    atividade_list = AtividadeModel.objects.all()
    atividade_form = AtividadeForm()
    form = ParceiroForm()
    return render(request, 'canvas/canvas_list.html', {
        'list_canvas_model': list_canvas_model,
        'atividade_list': atividade_list,
        'atividade_form': atividade_form,
        'form': form
        }
    )


def canvas_add(request):
    form = ParceiroForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    atividade = AtividadeForm(request.POST or None)
    if atividade.is_valid():
        atividade.save()

    return redirect('canvas_list')
