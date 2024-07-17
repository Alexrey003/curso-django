from django.shortcuts import render
import datetime


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def saludo(request):
        
        persona1 = Persona("Alexis", "Reynoso")
        
        fecha_actual = datetime.datetime.now()
        
        temas = ['Plantillas', 'Modelos', 'BBDD', 'Formularios', 'Vistas', 'Email']
        
        ctx ={
            'name' : persona1.nombre,
            'last_name' : persona1.apellido,
            'today_date' : fecha_actual,
            'content' : temas,
        }
        
        return render(request, 'index.html', ctx)

    def curso_django(request):
                
        persona1 = Persona("Alexis", "Reynoso")
        
        fecha_actual = datetime.datetime.now()
        
        temas = ['Plantillas', 'Modelos', 'BBDD', 'Formularios', 'Vistas', 'Email']
        
        ctx ={
            'name' : persona1.nombre,
            'last_name' : persona1.apellido,
            'today_date' : fecha_actual,
            'content' : temas,
        }
        
        return render(request, 'curso-django.html', ctx)