from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import MaricularMaterias

# Create your views here.
def home(request):
    materias = MaricularMaterias.objects.all().order_by("nombre")
    contexto = {"materias": materias}
    return render(request, "gestionMaterias.html", context=contexto)


#@login_required
def register_topic(request):
    if request.method == "POST":
        codigo = request.POST.get("codigo")
        nombre = request.POST.get("nombre")
        creditos = request.POST.get("creditos")
        materias = MaricularMaterias.objects.create(id=codigo, nombre=nombre, creditos=creditos)
        materias.save()
        messages.success(request, '¡Materia matriculada con exito!')

        return redirect("home")
    
    return render(request, "gestionMaterias.html")


def update_topic(request):
    return render(request, "actualizar.html")


def delete_topic(request, pk: int):
    materias = MaricularMaterias.objects.get(id=pk)
    materias.delete()
    return redirect("home")


def info_user(request):
    return render(request, "contacto.html")



