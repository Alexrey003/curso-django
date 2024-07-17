from django.http import HttpResponse
from django.template import Template, Context
import datetime

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def saludo(request):
        
        persona1 = Persona("Valeria", "Rivero")
        
        # nombre = "Alexis"
        
        # apellido = "Reynoso"
        
        fecha_actual = datetime.datetime.now()
        
        temas = ['Plantillas', 'Modelos', 'BBDD', 'Formularios', 'Vistas', 'Email']
        # 
        
        doc_externo = open("C:/Users/Alexis/Desktop/ArchivosCurso/Django/ProyectosDjango/PlantillasIII/PlantillasIII/Templates/index.html")
        
        plt = Template(doc_externo.read())
        doc_externo.close()
        
        ctx = Context({
            'name' : persona1.nombre,
            'last_name' : persona1.apellido,
            'name_2' : 'Valeria',
            'last_name_2' : 'Rivero',
            'today_date' : fecha_actual,
            'content' : temas,
        })
        
        documento = plt.render(ctx)
        
        return HttpResponse(documento)
