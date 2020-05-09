from django.db import models
from django.shortcuts import reverse
from django_extensions.db.fields import AutoSlugField

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    cuerpo = models.TextField()
    autor = models.ForeignKey("Autor", on_delete=models.PROTECT)
    fecha_publicacion = models.DateTimeField()
    slug = AutoSlugField(max_length=50, unique=True, populate_from=('titulo', 'autor__nombre'))

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        """ retorna el url de la vista detalle del producto """
        return reverse("posteos:posts", kwargs={
            "slug": self.slug,
        })

class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    fehca_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=200)
    nacionalidad = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
