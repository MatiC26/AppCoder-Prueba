from django.contrib import admin
from django.urls import path
from listado.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumnos/', lista_alumnos2)
]
