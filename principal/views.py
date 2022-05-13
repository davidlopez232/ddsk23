from django.conf import settings
from django.shortcuts import render
from .models import Departamento
from django.conf import settings
from django.core.mail import send_mail

def inicio(request):
    Departamentos = Departamento.objects.all()
    contexto = {
        'Departamentos':Departamentos
    }
    return render(request, 'index.html', contexto)

def formularioContacto(request):
    return render(request, 'formularioContacto.html')

def contactar(request):
    if request.method == "POST":
        asunto = request.POST ["txtAsunto"]
        mensaje = request.POST ["txtMensaje"] + " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["kasekage233@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contactoExitoso.html")
    return render(request, "formularioContato.html")

