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
    ReceitaForm,
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
    ReceitaModel,
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
    receita_list = ReceitaModel.objects.all()
    receita_form = ReceitaForm()
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
        'receita_list': receita_list,
        'receita_form': receita_form,
        }
    )


#_________________________Start Parceiro___________________________
def parceiro_add(request):
    form = ParceiroForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')


def parceiro_update(request, id):
    update = ParceiroModel.objects.get(id=id)
    form = ParceiroForm(request.POST or None, instance=update)
    data = {
        'update': update,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('canvas_list')
    else:
        return render(request, 'canvas/parc_update.html', data)


def parceiro_delete(request, id):
    parceiro = ParceiroModel.objects.get(id=id)
    if request.method == 'POST':
        parceiro.delete()
        return redirect('canvas_list')
    else:
        return render(request, 'canvas/confirm_delete.html', {'obj': parceiro})
#_________________________The End Parceiro_____________________________


#_________________________Start Atividade______________________________
def atividade_add(request):
    form = AtividadeForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')


def atividade_update(request, id):
    update = AtividadeModel.objects.get(id=id)
    form = AtividadeForm(request.POST or None, instance=update)
    data = {
        'update': update,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('canvas_list')
    else:
        return render(request, 'canvas/ativ_update.html', data)


def atividade_delete(request, id):
    atividade = AtividadeModel.objects.get(id=id)
    if request.method == 'POST':
        atividade.delete()
        return redirect('canvas_list')
    else:
        return render(request, 'canvas/confirm_delete.html', {'obj': atividade})
#_________________________The end Atividade______________________________


#_________________________Start Recurso__________________________________
def recurso_add(request):
    form = RecursoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')


def recurso_update(request, id):
    update = RecursoModel.objects.get(id=id)
    form = RecursoForm(request.POST or None, instance=update)
    data = {
        'update': update,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('canvas_list')
    else:
        return render(request, 'canvas/rec_update.html', data)


def recurso_delete(request, id):
    recurso = RecursoModel.objects.get(id=id)
    if request.method == 'POST':
        recurso.delete()
        return redirect('canvas_list')
    else:
        return render(request, 'canvas/confirm_delete.html', {'obj': recurso})
#_________________________ The end Recurso ________________________________


#_________________________ Start Proposta _________________________________
def proposta_add(request):
    form = PropostaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')


def proposta_update(request, id):
    update = PropostaModel.objects.get(id=id)
    form = PropostaForm(request.POST or None, instance=update)
    data = {
        'update': update,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('canvas_list')
    else:
        return render(request, 'canvas/prop_update.html', data)
#_________________________ The end Proposta _______________________________


#_________________________ Start Relacionamento ___________________________
def rel_add(request):
    form = RelForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')


def rel_update(request, id):
    update = RelModel.objects.get(id=id)
    form = RelForm(request.POST or None, instance=update)
    data = {
        'update': update,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('canvas_list')
    else:
        return render(request, 'canvas/rel_update.html', data)
#_________________________ The end Relacionamento _______________________


#_________________________ Start Canal __________________________________
def canal_add(request):
    form = CanalForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')


def canal_update(request, id):
    update = CanalModel.objects.get(id=id)
    form = CanalForm(request.POST or None, instance=update)
    data = {
        'update': update,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('canvas_list')
    else:
        return render(request, 'canvas/canal_update.html', data)
#_________________________ The end Canal ____________________________________________


#_________________________ Start Segmento ___________________________________________
def segmento_add(request):
    form = SegmentoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')


def segmento_update(request, id):
    update = SegmentoModel.objects.get(id=id)
    form = SegmentoForm(request.POST or None, instance=update)
    data = {
        'update': update,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('canvas_list')
    else:
        return render(request, 'canvas/seg_update.html', data)
#_________________________ The end Segmento __________________________________________


#_________________________ Start Custo _______________________________________________
def custo_add(request):
    form  = CustoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')


def custo_update(request, id):
    update = CustoModel.objects.get(id=id)
    form = CustoForm(request.POST or None, instance=update)
    data = {
        'update': update, 
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('canvas_list')
    else:
        return render(request, 'canvas/custo_update.html', data)
#_________________________ The end Custo ______________________________________________


#_________________________ Start Receita ______________________________________________
def receita_add(request):
    form = ReceitaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('canvas_list')

def receita_update(request, id):
    update = ReceitaModel.objects.get(id=id)
    form = ReceitaForm(request.POST or None, instance=update)
    data = {
        'update': update,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('canvas_list')
    else:
        return render(request, 'canvas/receita_update.html', data)
#_________________________ The end Receita ____________________________________________
