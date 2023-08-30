from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import MaricularMaterias
from django.db.models import Q
from crearUsuario.models import RegistroDeUsuario


# Create your views here.
def home(request):
    materias = MaricularMaterias.objects.all().order_by("nombre")
    contexto = {"materias": materias}
    return render(request, "gestionMaterias.html", context=contexto)



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
    if request.method == "POST":
        codigo = request.POST.get("codigo")
        nombre = request.POST.get("nombre")
        creditos = request.POST.get("creditos")
        
        try:
            topic = MaricularMaterias.objects.get(id=codigo)
            topic.nombre = nombre
            topic.creditos = creditos
            topic.save()
            
            messages.success(request, "¡Matricula actualizada con éxito!")

        except MaricularMaterias.DoesNotExist:
            messages.error(request, "¡No se encontró la materia!")

    return render(request, "actualizar.html")


def delete_topic(request, pk: int):
    materias = MaricularMaterias.objects.get(id=pk)
    materias.delete()
    return redirect("home")


def info_user(request):
    return render(request, "contacto.html")


def search_topic(request):
    query = request.GET.get("q")
    if query:
        results = MaricularMaterias.objects.filter(Q(nombre__icontains=query))
    else:
        results = []

        context = {
            'results': results,
            'query': query}
        
        return render(request, 'search.html', context)



