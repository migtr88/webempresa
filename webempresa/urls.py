"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
#from  services import views as services_views
urlpatterns = [
    #Paths del core
   path('', include('appcore.urls')),
   #path services 
   path('services/',include('services.urls')),
   path('blog/', include('blog.urls')),
   path('page/',include('pages.urls')),
   path('contact/',include('contact.urls')),
    #Paths del admin
    path('admin/', admin.site.urls),
]
#Para servir ficheros de media 
if settings.DEBUG:
    from django.conf.urls.static import static
    # indicamos url de media y dirección del directorio donde estarán las imagenes (importadas de settings)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)