from django.http import HttpResponse
from django.template import Template, Context
import datetime

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def plantillas_II(request):
        
        # nombre = "Alexis"
        # apellido ='Reynoso'
        
        persona1 = Persona('Alexis','Munive')
        fecha = datetime.datetime.now()
        
        html = open('C:/Users/Alexis/Desktop/ArchivosCurso/Django/ProyectosDjango/PlantillasII/PlantillasII/Templates/index.html')
        
        plt = Template(html.read())
        
        html.close()
        
        ctx = Context({
            'name' : persona1.nombre,
            'last_name' : persona1.apellido,
            'name_2' : 'Valeria',
            'last_name_2' : 'Rivero',
            'today_date' : fecha
        })
        
        render = plt.render(ctx)
        
        return HttpResponse(render)