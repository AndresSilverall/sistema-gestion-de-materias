from django.shortcuts import render, redirect
from django.contrib import messages
from . models import MaricularMaterias

# Create your views here.
def home(request):
    materias = MaricularMaterias.objects.all().order_by("nombre")
    contexto = {"materias": materias}
    return render(request, "gestionMaterias.html", context=contexto)


def register_topic(request):
    codigo = request.POST.get("codigo")
    nombre = request.POST.get("nombre")
    creditos = request.POST.get("creditos")
    if request.method == "POST":
        materias = MaricularMaterias.objects.create(id=codigo, nombre=nombre, creditos=creditos)
        materias.save()
        messages.success(request, '¡Materia matriculada con exito!')

        return redirect("home")
    
    return render(request, "gestionMaterias.html")


def delete_topic(request, pk: int):
    materias = MaricularMaterias.objects.get(id=pk)
    materias.delete()
    return redirect("home")



def info_user(request):
    return render(request, "contacto.html")



