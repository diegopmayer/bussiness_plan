from django.urls import path
from .views import (
    canvas_list,
    parceiro_add,
    atividade_add,
    recurso_add,
    proposta_add,
    rel_add,
    canal_add,
    segmento_add,
    custo_add,
    receita_add,
    parceiro_update,
    atividade_update,
    recurso_update,
)

urlpatterns = [
    path('list', canvas_list, name='canvas_list'),
    path('parceiro-add', parceiro_add, name='parceiro_add'),
    path('parceiro-update/<int:id>/', parceiro_update, name='parceiro_update'),
    path('atividade-add', atividade_add, name='atividade_add'),
    path('atividade-update/<int:id>/', atividade_update, name='atividade_update'),
    path('recurso-add', recurso_add, name='recurso_add'),
    path('recurso-update/<int:id>/', recurso_update, name='recurso_update'),
    path('proposta-add', proposta_add, name='proposta_add'),
    path('rel-add', rel_add, name='rel_add'),
    path('canal-add', canal_add, name='canal_add'),
    path('segmento-add', segmento_add, name='segmento_add'),
    path('custo-add', custo_add, name='custo_add'),
    path('receita-add', receita_add, name='receita_add'),
]
