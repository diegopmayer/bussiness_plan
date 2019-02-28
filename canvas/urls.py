from django.urls import path
from .views import canvas_view
urlpatterns = [
    path('', canvas_view , name='canvas_view')
]