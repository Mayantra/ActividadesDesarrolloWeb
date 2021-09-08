from django.contrib import admin
from .models import Administrador, Articulo, Comentario, Estudiante  

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Administrador)
admin.site.register(Articulo)
admin.site.register(Comentario)
