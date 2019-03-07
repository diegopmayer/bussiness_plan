from django.urls import path
from .views import canvas_list, canvas_view

urlpatterns = [
    path('list', canvas_list, name='canvas_list'),
    path('', canvas_view, name='canvas_view')
]