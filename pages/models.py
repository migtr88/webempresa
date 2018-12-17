from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Page(models.Model):
      #el campo de tipo Slug nos obligará a q la clave sea alfanumérica 
    title = models.CharField(verbose_name = "Tìtulo", max_length=200 )
   #Sustituimos el campo TextField de Django por el editor ckeditor, RECORDAR modificar la configuración de Settings
   # content = models.TextField(verbose_name = "Contenido",)
    content = RichTextField(verbose_name = "Contenido")
    #Campo para ordenar el modelo, indicara el orden según el cuál se mostrará cada modelo
    order = models.SmallIntegerField(verbose_name="Orden",default=0)
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de actualización ")
    class Meta: 
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order','title']
    
    def __str__(self):
        return self.title