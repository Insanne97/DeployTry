from django.db import models

# Create your models here.
class Registros(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    materia = models.CharField(max_length=30)

    # Visuacion de objetos con datos del usuario registrado
    def __str__(self):
        text = "{0} {1}"
        return text.format(self.nombre, self.apellido, self.correo, self.materia)