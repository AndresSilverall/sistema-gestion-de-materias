from django.shortcuts import render, redirect
from . models import MaricularMaterias

# Create your views here.
def home(request):
    materias = MaricularMaterias.objects.all()
    contexto = {"materias": materias}
    return render(request, "gestionMaterias.html", context=contexto)


def register_topic(request):
    id = request.POST["codigo"]
    nombe = request.POST["nombre"]
    creditos = request.POST["creditos"]
    if request.method == "POST":
        materias = MaricularMaterias.objects.create(id=id, nombre=nombe, creditos=creditos)
        materias.save()
        redirect("register")
    return render(request, "gestionMaterias.html")


def info_user(request):
    return render(request, "contacto.html")

