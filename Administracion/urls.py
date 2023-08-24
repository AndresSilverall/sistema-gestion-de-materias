from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("GestionarMaterias.urls")),
    path('', include("login.urls")),
    path('', include("crearUsuario.urls")),
]
