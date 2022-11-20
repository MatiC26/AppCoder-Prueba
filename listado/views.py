from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from django.template import loader

def lista_alumnos(request):
    
    archivo = open(r"C:/Users/matic/OneDrive/Escritorio/proyectos/proyecto-alumnos/listado/templates/listado_alumnos.html")
    plantilla = Template(archivo.read())
    
    archivo.close()
    
    listado_alumnos = ["Matias Carignano", "Tomas Pandullo", "Juan Buongiorno"]
    
    datos = {"tecnologia": "React", "alumnos": listado_alumnos }
    
    contexto = Context(datos) 
    
    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)

def lista_alumnos2(request):
   listado_alumnos = ["Matias Carignano", "Tomas Pandullo", "Juan Buongiorno"]
   datos = {"tecnologia": "React", "alumnos": listado_alumnos}
   
   plantilla = loader.get_template("listado_alumnos.html")
   documento = plantilla.render(datos)

   return HttpResponse(documento) 