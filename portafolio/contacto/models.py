from django.db import models

# Create your models here.
from django.db import models


class Mensaje(models.Model):
    nombre = models.CharField(max_length=100, default='')
    asunto = models.CharField(max_length=150, default='')
    email = models.EmailField(max_length=50)
    comentarios = models.TextField(max_length=400)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} - {self.asunto} - {self.email} - {self.comentarios} - {self.telefono} "
