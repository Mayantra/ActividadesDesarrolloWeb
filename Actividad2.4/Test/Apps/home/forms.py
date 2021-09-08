from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import widgets
from .models import Administrador, Estudiante

class FormEstudiante(forms.ModelForm):

    class Meta:
        model = Estudiante
        
        fields= [
            'nombres',
            'apellidos',
            'direccion',
            'carne',
            

        ]
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'direccion': 'Direccion',
            'carne': 'Carné',
        }
        widgets = {
            'nombres': forms.TextInput(),
            'apellidos': forms.TextInput(),
            'direccion': forms.TextInput(),
            'carne': forms.TextInput(),
        }
class FormAdmins(forms.ModelForm):
    class Meta:
        model= Administrador
        
        fields= [
            'nombres',
            'apellidos',
            'direccion',
            'carne',
            

        ]
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'direccion': 'Direccion',
            'carne': 'Carné',
        }
        widgets = {
            'nombres': forms.TextInput(),
            'apellidos': forms.TextInput(),
            'direccion': forms.TextInput(),
            'carne': forms.TextInput(),
        }