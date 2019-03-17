from django.shortcuts import render


def index(request):
    return render(request, 'bus_plan/index.html')
