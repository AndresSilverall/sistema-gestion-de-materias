from django.shortcuts import render, redirect
from django.contrib import messages
from . models import MaricularMaterias

# Create your views here.
def home(request):
    materias = MaricularMaterias.objects.all().order_by("nombre")
    contexto = {"materias": materias}
    return render(request, "gestionMaterias.html", context=contexto)


def register_topic(request):
    id = request.POST["codigo"]
    nombre = request.POST["nombre"]
    creditos = request.POST["creditos"]
    if request.method == "POST":
        materias = MaricularMaterias.objects.create(id=id, nombre=nombre, creditos=creditos)
        materias.save()
        messages.success(request, '¡Materia matriculada con exito!')

        return redirect("register")
    
    return render(request, "gestionMaterias.html")


def info_user(request):
    return render(request, "contacto.html")


def form_login(request):
    return render(request, "login.html")
