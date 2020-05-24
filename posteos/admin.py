from django.contrib import admin
from django.db import models
from .models import Post, Autor, Mail
from tinymce.widgets import TinyMCE

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Post, PostAdmin)
admin.site.register(Autor)
admin.site.register(Mail)


admin.AdminSite.site_header = "Administración de Vox Populi"
admin.AdminSite.site_title = "Administración de Vox Populi"
