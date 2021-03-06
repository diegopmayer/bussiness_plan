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
    proposta_update,
    rel_update,
    canal_update,
    segmento_update,
    custo_update,
    receita_update,
    parceiro_delete,
    atividade_delete,
    recurso_delete,
    proposta_delete,
    rel_delete,
    canal_delete,
    segmento_delete,
    custo_delete,
    receita_delete,
)

urlpatterns = [
    path('list', canvas_list, name='canvas_list'),

    path('parceiro-add', parceiro_add, name='parceiro_add'),
    path('parceiro-update/<int:id>/', parceiro_update, 
        name='parceiro_update'),
    path('parceiro-delete/<int:id>/', parceiro_delete, name="parceiro_delete"),

    path('atividade-add', atividade_add, name='atividade_add'),
    path('atividade-update/<int:id>/', atividade_update, 
        name='atividade_update'),
    path('atividade-delete/<int:id>/', atividade_delete, name="atividade_delete"),

    path('recurso-add', recurso_add, name='recurso_add'),
    path('recurso-update/<int:id>/', recurso_update, 
        name='recurso_update'),
    path('recurso-delete/<int:id>/', recurso_delete, name='recurso_delete'),

    path('proposta-add', proposta_add, name='proposta_add'),
    path('proposta-update/<int:id>/', proposta_update, 
        name='proposta_update'),
    path('proposta-delete/<int:id>/', proposta_delete, name='proposta_delete'),
    
    path('rel-add', rel_add, name='rel_add'),
    path('rel-update/<int:id>/', rel_update, name='rel_update'),
    path('rel-delete/<int:id>/', rel_delete, name='rel_delete'),

    path('canal-add', canal_add, name='canal_add'),
    path('canal-update/<int:id>/', canal_update, name='canal_update'),
    path('canal-delete/<int:id>/', canal_delete, name='canal_delete'),

    path('segmento-add', segmento_add, name='segmento_add'),
    path('segmento-update/<int:id>/', segmento_update, 
        name='segmento_update'),
    path('segmento-delete/<int:id>/', segmento_delete, name="segmento_delete"),

    path('custo-add', custo_add, name='custo_add'),
    path('custo-update/<int:id>/', custo_update, name='custo_update'),
    path('custo-delete/<int:id>/', custo_delete, name='custo_delete'),

    path('receita-add', receita_add, name='receita_add'),
    path('receita-update/<int:id>/', receita_update, name='receita_update'),
    path('receita-delete/<int:id>/', receita_delete, name='receita_delete'),
]
