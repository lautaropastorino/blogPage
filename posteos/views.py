from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post, Mail
from django.views.generic import DetailView, ListView
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from datetime import datetime

def homepage(request):
    try:
        articulos = Post.objects.order_by('-fecha_publicacion')
        context = {
            "ultimo": articulos[0],
            "articulos": articulos[:10],
        }
        return render(request, "homepage.html", context=context)
    except IndexError:
        return render(request, "homepage.html")

def suscribirse(request):
        return render(request, "suscribirse.html")

def enviar_mi_contenido(request):
        return render(request, "enviar_mi_contenido.html")

def registrar_mail(request):
    import json
    from django.core.exceptions import ValidationError
    from django.core.validators import validate_email
    body = request.body  #POST DATA
    email = json.loads(body)["mail"] #Leo desde json
    try:
        validate_email(email)
        obj, created  = Mail.objects.get_or_create(direccion=email)
        if created:
            data = {"exito": True, "mensaje": "Dirección registrada correctamente"}
        else:
            data = {"exito": False, "mensaje": "La direccion ya estaba registrada"}
    except ValidationError as e:
        data = {"exito": True, "mensaje": f"Error en la dirección ingresada: {e.message}"}
    return JsonResponse(data)

class PostView(DetailView):
    #View generica para detalle de un modelo
    model = Post
    template_name = "post-page.html"

class AllView(ListView):
    #View generica para detalle de un modelo
    model = Post
    template_name = "all-posts.html"

class SearchView(ListView):
    model = Post
    template_name = "search-results.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(titulo__icontains=query) | Q(cuerpo__icontains=query) | Q(autor__nombre__icontains=query)
        )
        return object_list
