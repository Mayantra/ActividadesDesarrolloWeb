from django.contrib import admin
from .models import Cliente, TipoCliente, Ventas

# Register your models here.
admin.site.register(Cliente)
admin.site.register(TipoCliente)
admin.site.register(Ventas)