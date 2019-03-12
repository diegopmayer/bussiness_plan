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
)

urlpatterns = [
    path('list', canvas_list, name='canvas_list'),
    path('parceiro-add', parceiro_add, name='parceiro_add'),
    path('atividade-add', atividade_add, name='atividade_add'),
    path('recurso-add', recurso_add, name='recurso_add'),
    path('proposta-add', proposta_add, name='proposta_add'),
    path('rel-add', rel_add, name='rel_add'),
    path('canal-add', canal_add, name='canal_add'),
    path('segmento-add', segmento_add, name='segmento_add'),
]
