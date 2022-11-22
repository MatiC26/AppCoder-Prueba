from django.http import HttpResponse
from AppCoder.models import Curso
from django.shortcuts import render

def inicio(request):
   return render(request, "AppCoder/index.html")

def cursos(request):
   return HttpResponse("Estas en cursos")

def estudiantes(request):
   return HttpResponse("Estas en estudiantes")

def profesores(request):
   return HttpResponse("Estas en profesores")
    
    
def entregables(request):
   return HttpResponse("Estas en entregables")
    
pass
