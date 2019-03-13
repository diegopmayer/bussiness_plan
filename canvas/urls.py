from django.urls import path
from .views import canvas_list, parceiro_add, atividade_add

urlpatterns = [
    path('list', canvas_list, name='canvas_list'),
    path('parceiro-add', parceiro_add, name='parceiro_add'),
    path('atividade-add', atividade_add, name='atividade_add'),
]
