from django.shortcuts import render, redirect
from django.http import HttpResponseServerError
from django.contrib import messages
from django.contrib.auth import authenticate, login
from crearUsuario.models import RegistroDeUsuario

def form_login(request):
    user = RegistroDeUsuario.objects.get(id=1)
    context = {
        "user": user
        }
    if request.method == "POST":
        correo = request.POST.get("correo")
        contraseña = request.POST.get("contraseña")

        try: 
            user_registered = authenticate(correo=correo, contraseña=contraseña)
            if user_registered is not None:
                login(request, user_registered)

        except RegistroDeUsuario.DoesNotExist:
            user_registered = None
            return HttpResponseServerError("error")

        else:
            error_message = "Correo o contraseña invalidos, por favor intenta de nuevo"
            return render(request, 'login.html', {'error_message': error_message})

    
    return render(request, "login.html", context=context)