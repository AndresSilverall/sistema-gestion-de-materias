from django.shortcuts import render, redirect
from django.contrib import messages
from .models import RegistroDeUsuario


def create_user(request):
    nombre = request.POST.get("nombre")
    correo = request.POST.get("correo")
    contraseña = request.POST.get("contraseña")

    if request.method == "POST":
        registro = RegistroDeUsuario.objects.create(nombre=nombre, correo=correo, contraseña=contraseña)
        registro.save()
        messages.success(request,"Usuario registrado con exito!")
        return redirect("create_user")

    return render(request, "createUser.html")
