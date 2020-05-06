from django.db import models
from django.shortcuts import reverse
from django_extensions.db.fields import AutoSlugField

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    bajada = models.CharField(max_length=100)
    cuerpo = models.TextField()
    fecha_publicacion = models.DateTimeField()
    slug = AutoSlugField(max_length=50, unique=True, populate_from=('titulo', 'bajada'))

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        """ retorna el url de la vista detalle del producto """
        return reverse("posteos:posts", kwargs={
            "slug": self.slug,
        })
