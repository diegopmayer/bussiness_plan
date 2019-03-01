from django.shortcuts import render
from .form import CanvasForm

def canvas_view(request):
    canvas_form = CanvasForm(request.POST or None)
    context={
        'form': canvas_form,
    }
    return render(request, 'canvas/canvas.html', context)