from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case
from django.db.models.fields import CharField
from django.db.models.fields.mixins import FieldCacheMixin

""" # Create your models here.
class Cliente(models.Model):

    doc = (
        ('D','DPI'),
        ('C','Cedula')
    )
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    nacimiento = models.DateField()
    tipo =models.ForeignKey('TipoCliente', on_delete=models.CASCADE,default=1)
    documento = models.CharField(max_length=20, choices=doc,default='D')
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class TipoCliente(models.Model):
    tipo = models.CharField(max_length=10)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return '%s' % (self.tipo)

class Ventas(models.Model):
    cliente = models.ManyToManyField(Cliente)
    fecha = models.DateTimeField() """




class Estudiante(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    carne = models.CharField(max_length=20)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombres, self.apellidos)

class Administrador(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    carne = models.CharField(max_length=20)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombres, self.apellidos)

class Articulo(models.Model):
    titulo = models.CharField(max_length= 20)
    contenido = models.TextField(max_length= 2000)
    fecha = models.DateTimeField()

    estudiante = models.ForeignKey('Estudiante', on_delete=CASCADE, default=1)
    administrador = models.ForeignKey('Administrador', on_delete=CASCADE, default=1)

    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.titulo)

class Comentario(models.Model):
    contenido = models.CharField(max_length=500)
    fecha = models.DateTimeField()

    estudiante = models.ForeignKey('Estudiante', on_delete=CASCADE, default=1)
    articulo = models.ForeignKey('Articulo', on_delete=CASCADE, default=1)

    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.estudiante)

