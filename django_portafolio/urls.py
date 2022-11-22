from django.contrib import admin
from django.urls import path, include
from listado.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumnos/', lista_alumnos2),
    
    path("coder/", include("AppCoder.urls"))
]
