
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView


from Apps.home.models import Estudiante
from Apps.home.forms import FormEstudiante

# Create your views here.
class HomeView(TemplateView):
    template_name='index.html'

class EstudiantesView(TemplateView):
    template_name='Estudiantes.html'

class AdminsView(TemplateView):
    template_name='Administradores.html'

class AcercaView(TemplateView):
    template_name='AcercaDe.html'

class EstuDesta(TemplateView):
    template_name='EstuDestacados.html'


class FormEstudianteView(CreateView):
    model = Estudiante
    form_class = FormEstudiante
    template_name='EstudiantesForms.html'
    
    
