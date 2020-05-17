from django.db import models
from django.shortcuts import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models.signals import post_save
from django.dispatch import receiver


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

class Mail(models.Model):
    direccion = models.EmailField(unique=True)

    def __str__(self):
        return self.direccion


@receiver(post_save, sender=Post)
def enviar_mails(sender, instance, created, **kwargs):
    from django.conf import settings
    from django.template.loader import render_to_string
    from django.core.mail import EmailMultiAlternatives
    from smtplib import SMTPException
    if created:
        #intance es el post
        post = instance
        emailSubject = post.titulo
        emailOfSender = settings.EMAIL_HOST_USER
        context = ({
            "titulo": post.titulo,
            "autor": post.autor.nombre,
            "url": post.get_absolute_url
        })
        text_content = render_to_string('new_post_email.txt', context)
        html_content = render_to_string('new_post_email.html', context)

        for d in Mail.objects.all():
            try:
                emailMessage = EmailMultiAlternatives(subject=emailSubject, body=text_content, from_email=emailOfSender, to=[d.direccion], reply_to=[emailOfSender])
                emailMessage.attach_alternative(html_content, "text/html")
                emailMessage.send(fail_silently=False)
            except SMTPException as e:
                print('There was an error sending an email: ', e)
                error = {'message': ",".join(e.args) if len(e.args) > 0 else 'Unknown Error'}
                raise serializers.ValidationError(error)
