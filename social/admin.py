from django.contrib import admin
from .models import Link
# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "updated"]
#Para extender la función de readonly_fields en tiempo de ejecución, es decir q cuando se esta ejecutando la aplicación 
#se pueda hacer que determinados campos sean solo de lectura, nos interesa hacerlo para ciertos usuarios,declaramos el método
    def get_readonly_fields(self, request, obj=None):
        #si el usuario pertenece al grupo de usuarios de Personal 
        if request.user.groups.filter(name = "Personal"):
            #devolvemos como readonly_fields los campos del modelo de appsocial q nos interesa dejar de lectura
            return('created','updated','key','name')
        #si no fuera así devolvemos los normales 
        else:
            return('created','updated')


admin.site.register(Link, LinkAdmin)