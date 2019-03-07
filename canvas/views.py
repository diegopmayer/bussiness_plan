from django.shortcuts import render
from .form import CanvasForm
from .models import CanvasModel


def canvas_view(request):
    canvas_form = CanvasForm(request.POST or None)
    context={
        'form': canvas_form,
    }
    return render(request, 'canvas/canvas.html', context)


def canvas_list(request):
    list_canvas_model = CanvasModel.objects.all()
    return render(request, 'canvas/canvas_list.html', {'list_canvas_model': list_canvas_model})
