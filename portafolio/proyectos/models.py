from django.db import models

# modelo para guardar mis proyectos


class proyectos(models.Model):

    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='portafolio/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.descripcion}"
