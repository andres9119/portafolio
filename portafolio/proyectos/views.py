from django.shortcuts import render
from .models import proyectos

# Vista para el modelo proyectos


def lista_proyectos(request):
    proyectos_list = proyectos.objects.all()
    return render(request, 'proyectos/lista_proyectos.html', {'proyectos_list': proyectos_list})
