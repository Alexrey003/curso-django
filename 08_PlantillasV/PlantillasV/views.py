from django.http import HttpResponse
# from django.template import Template, Context, loader
from django.shortcuts import render
import datetime


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def saludo(request):
        
        persona1 = Persona("Alexis", "Reynoso")
        
        # nombre = "Alexis"
        
        # apellido = "Reynoso"
        
        fecha_actual = datetime.datetime.now()
        
        temas = ['Plantillas', 'Modelos', 'BBDD', 'Formularios', 'Vistas', 'Email']
        
        # doc_html = loader.get_template('index.html')
        
        ctx ={
            'name' : persona1.nombre,
            'last_name' : persona1.apellido,
            # 'name_2' : 'Valeria',
            # 'last_name_2' : 'Rivero',
            'today_date' : fecha_actual,
            'content' : temas,
        }
        
        # doc_render = doc_html.render(ctx)
        
        return render(request, 'index.html', ctx)

    def curso_django(request):
                
        persona1 = Persona("Alexis", "Reynoso")
        
        # nombre = "Alexis"
        
        # apellido = "Reynoso"
        
        fecha_actual = datetime.datetime.now()
        
        temas = ['Plantillas', 'Modelos', 'BBDD', 'Formularios', 'Vistas', 'Email']
        
        # doc_html = loader.get_template('index.html')
        
        ctx ={
            'name' : persona1.nombre,
            'last_name' : persona1.apellido,
            # 'name_2' : 'Valeria',
            # 'last_name_2' : 'Rivero',
            'today_date' : fecha_actual,
            'content' : temas,
        }
        
        # doc_render = doc_html.render(ctx)
        
        return render(request, 'curso-django.html', ctx)