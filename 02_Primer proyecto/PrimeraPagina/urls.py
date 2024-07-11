from django.contrib import admin
from django.urls import path
from PrimeraPagina.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('primer-vista/', saludo),
    path('segunda-vista/', despedida),
]
