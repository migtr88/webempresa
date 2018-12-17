from django.contrib import admin
from .models import Category,Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']

admin.site.register(Category,CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
   readonly_fields = ['created', 'updated']
    #Indicamos que columnas queremos q se muestren en el admin de django
   list_display = ['title','author','published', 'post_categories']
   #ordenamos por un campo y luego dentro de ese campo por otro campo 
   ordering = ['author', 'published']
   #Buscamos por un campo:  si es un modelo debe ser: modelo__campo 
   search_fields = ['title', 'content', 'author__username', 'categories__name']
   #Para poder buscar por fechas 
   date_hierarchy = 'published'
   #Para añadir filtros para determinados campos 
   list_filter = ('author__username', 'categories__name')
   #Para añadir un modelo relacionado como columna no se podria con list_display por lo que
   #necesitamos crear un método y pasarselo a list_display 
   def post_categories(self, obj):
        #join devuelve una cadena con todas las categorias ordenadas por nombre extraidas a traves del bucle que recorre todas las categorias 
        #que tiene el objeto que le pasemos que sera el post 
        return "," .join(c.name for c in obj.categories.all().order_by("name") )
        #Para establecer como titulo a esa columna un nombre propio en vez de el del método
        #sobreescribimos un atributo de los métodos 
   post_categories.short_description = "Categorías"

admin.site.register(Post,PostAdmin)