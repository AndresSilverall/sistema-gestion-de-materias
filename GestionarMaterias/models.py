from django.db import models

# Create your models here.
class MaricularMaterias(models.Model):
    id = models.CharField(primary_key=True,  max_length=5)
    nombre = models.CharField(max_length=40, blank=False, null=False)
    creditos = models.PositiveSmallIntegerField(blank=False, null=False)
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} ({}) {}".format(self.nombre, self.creditos, self.fecha)
