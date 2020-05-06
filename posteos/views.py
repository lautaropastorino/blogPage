from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import DetailView, ListView
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
            Q(titulo__icontains=query) | Q(cuerpo__icontains=query) | Q(bajada__icontains=query)
        )
        return object_list
