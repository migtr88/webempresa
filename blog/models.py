from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User 
from ckeditor.fields import RichTextField
# Create your models here.
#Creamos un modelo para las categorías y otro para las entradas 
class Category(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Nombre")
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de actualización ")
    
    class Meta: 
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ["-created"]
    
    def __str__(self):
        return self.name

#Modelo para las entradas
class Post(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "Título")
   # content = models.TextField(verbose_name = "Contenido")
    content = RichTextField(verbose_name = "Contenido")
    #le asignamos un valor por defecto a la fecha de publicación, el de la fecha actual 
    published = models.DateTimeField(verbose_name = "Fecha de publicación",default = now)
    #No obligamos al usuario a que ponga una imagen en el contenido , establecemos null y blank a true
    image = models.ImageField(upload_to = "blog", verbose_name = "Imagen",null = True, blank = True)
    #Enlazamos un autor con un usuario, una instancia con un modelo, CASCADE borrará todas las entradas de este autor si se elmina el usuario asociado
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    #Queremos escoger varias categorías para una entrada, una relación de muchos a muchos , related_name nos define el nombre para la relacion 
    # para poder ir a buscar la relación inversa como si fuera otro campo del modelo, ya que Django solo deja obteneral mediante modelo_set una vez 
    categories = models.ManyToManyField(Category, verbose_name= "Categorías", related_name = "get_posts")
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de actualización ")

    class Meta: 
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title