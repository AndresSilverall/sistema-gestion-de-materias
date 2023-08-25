from django.db import models

# Create your models here.
class RegistroDeUsuario(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False, unique=True)
    correo = models.EmailField(blank=False, null=False, unique=True)
    contraseña = models.SmallIntegerField(unique=True)

    def __str__(self):
        return "{}, {}, {}".formar(self.nombre, self.correo, self.contraseña)