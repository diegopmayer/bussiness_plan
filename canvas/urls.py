from django.urls import path
from .views import (
    canvas_list,
    parceiro_add,
    atividade_add,
    recurso_add,
    proposta_add,
    relacionamento_add,
)

urlpatterns = [
    path('list', canvas_list, name='canvas_list'),
    path('parceiro-add', parceiro_add, name='parceiro_add'),
    path('atividade-add', atividade_add, name='atividade_add'),
    path('recurso-add', recurso_add, name='recurso_add'),
    path('proposta-add', proposta_add, name='proposta_add'),
    path('relacionamento-add', relacionamento_add, name='relacionamento_add'),
]
