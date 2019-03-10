from django.urls import path
from .views import canvas_list, canvas_add

urlpatterns = [
    path('list', canvas_list, name='canvas_list'),
    path('canvas-add', canvas_add, name='canvas_add')
]
