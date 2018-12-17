#Creamos procesador de contexto para poder mostrar los enlaces sin necesidad de mandar un diccionario en cada vista 
#NOS PERMITE acceder en caulquier html a ese diccionario que pasamos por contexto , de manera que indicando la clave acedemos al valor 
#útil para mostar enlaces como en este caso. 
 #lo tenemos q añadir en SETTINGS 'Templates'-> 'context processors'
from.models import Link
def ctx_dict(request):
    #Creamos un diccionario 
    #lo tenemos q añadir en SETTINGS 'Templates'-> 'context processors'
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx