from django.http import HttpResponse
import datetime


#ESTO ES UN CONTENIDO ESTATICO
def saludo(request):
    documento_html = '''
    <html>
        <body>
            <h1>Saludos mundo de Django y Python</h1>
        </body>
    </html>
    '''
    
    return HttpResponse(documento_html)

#ESTO ES UNA VISTA DE CONTENIDO DINAMICO
def fecha_hora(request):
    fecha_actual = datetime.datetime.now()
    documento_html = f'''
    <html>
        <body>
            <h1>Fecha y hora actuales <br> {fecha_actual}</h1>
        </body>
    </html>
    '''
    return HttpResponse(documento_html)

#PASANDO PARÁMETROS DESDE LA URLS PARA LA FUNCION DE LA VISTA
def calculadora_edad(request, age, year):
    periodo = year - 2024
    edad_futura = age + periodo
    documento_html = f'''
    <html>
        <body>
            <h1>Calculadora de edad</h1>
            <p> Ingresa como parámetro de la url el año futuro del que deseas basarte para saber tu edad futura</p>
            <p>Tu edad en el año {year} es: {edad_futura}</p>
        </body>
    </html>
    '''
    return HttpResponse(documento_html)