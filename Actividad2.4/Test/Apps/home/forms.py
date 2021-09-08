from django import forms
from django.forms import widgets
from Apps.home.models import Estudiante

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
            'nombres': 'Nombre',
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