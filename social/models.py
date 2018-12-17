from django.db import models

# Create your models here.
class Link(models.Model):

    #el campo de tipo Slug nos obligará a q la clave sea alfanumérica 
    key = models.SlugField(verbose_name = "Clave", max_length = 100, unique = True )
    name = models.CharField(verbose_name = "Red social", max_length=200)
    url = models.URLField(verbose_name = "Enlace", max_length=200, null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de actualización ")
    class Meta: 
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ["name"]
    
    def __str__(self):
        return self.name