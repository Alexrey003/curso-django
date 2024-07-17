from django.http import HttpResponse
from django.template import Template, Context

def saludo_curso(request):
    #CADA QUE TRABAJEMOS CON PATH DEBEMOS USAR EN VEZ DE  USAREMOS \ ESTA /
    documento_externo = open('C:/Users/Alexis/Desktop/ArchivosCurso/Django/ProyectosDjango/Plantillas/Plantillas/Template/index.html')
    
    plt = Template(documento_externo.read()) #CREAMOS EL OBJETO DE TIPO TEMPLATE
    
    documento_externo.close() #CERRAMOS EL DOCUMENTO PARA NO CONSUMIR RECURSOS.
    
    ctx = Context() #CREAMOS EL CONTEXTO, EN ESTE CASO SERA VACIO
    
    documento_renderizado = plt.render(ctx) #RENDERIZAMOS EL TEMPLATE
    
    return HttpResponse(documento_renderizado) #RETORNAMOS EL DOCUMENTO RENDERIZADO COMO UNA RESPUESTA HTTP.