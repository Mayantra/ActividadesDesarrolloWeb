
from django.forms import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy


from .models import Administrador, Estudiante
from .forms import FormAdmins, FormEstudiante

# Create your views here.
class HomeView(TemplateView):
    template_name='index.html'

class EstudiantesView(ListView):
    
    model = Estudiante
    template_name='Estudiantes.html'
    

class AdminsView(ListView):
    model = Administrador
    template_name='Administradores.html'

class AcercaView(TemplateView):
    template_name='AcercaDe.html'

class EstuDesta(TemplateView):
    template_name='EstuDestacados.html'


class FormEstudianteView(CreateView):
    model = Estudiante
    form_class = FormEstudiante
    template_name='EstudiantesForms.html'
    success_url = reverse_lazy('estudiantesForms')

class FormAdminsView(CreateView):
    model = Administrador
    form_class = FormAdmins
    template_name='AdminsForms.html'
    success_url = reverse_lazy('adminsForms')

class LoginView(TemplateView):
    template_name = 'Login.html'
    
    
        


