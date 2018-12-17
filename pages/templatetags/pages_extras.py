#Creamos nuestro propio template tag 
#Queremos que nos devuelva la lista de páginas de aviso legal,cookies para mostrarlas 
from django import template
from pages.models import Page

#Para registrarlo en la librería de templates 
register = template.Library()
#Añadimos un decorador para convertirlo en un tag simple
@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages 