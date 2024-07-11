'''HttpResponse hare que  cuando el usuario hagauna HttpRequest. la página le devolvera el HttpResponse'''
from django.http import HttpResponse

#Primera vista
def saludo(request):
    return HttpResponse("Hola mundo de Django y Python")

def despedida(request):
    return HttpResponse("Adiós mundo de Django y Python")