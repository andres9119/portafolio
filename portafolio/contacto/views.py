from django.shortcuts import render, redirect
from django.contrib import messages
from . import views
from .models import Mensaje

# Create your views here.


def contacto(request):

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        asunto = request.POST.get('asunto')
        email = request.POST.get('email')
        comentarios = request.POST.get('comentarios')
        telefono = request.POST.get('telefono')

        # Guardar los datos en la base de datos
        mensaje = Mensaje(
            nombre=nombre, asunto=asunto,  telefono=telefono,
            email=email, comentarios=comentarios)
        mensaje.save()

        # Agregar un mensaje flash de envio exitoso
        messages.success(request, '¡El formulario se ha enviado con éxito!')

        # Redirigir al usuario a la página de contacto nuevamente
        return redirect('contacto')

    return render(request, 'contacto.html')
