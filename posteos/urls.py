from django.urls import path
from . import views

app_name = "posteos"

urlpatterns = [
    path("", views.homepage, name="homapage"),
    path("posts/<slug>/", views.PostView.as_view(), name="posts"),
    path("post-list/", views.AllView.as_view(), name="all-posts"),
    path("search-results/", views.SearchView.as_view(), name="search-results"),
    path("registrar_mail", views.registrar_mail, name="registrar_mail")
]
