from django.shortcuts import render, redirect
from . models import MaricularMaterias

# Create your views here.
def home(request):
    materias = MaricularMaterias.objects.all()
    contexto = {"materias": materias}
    return render(request, "gestionMaterias.html", context=contexto)
