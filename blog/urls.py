#URL's de blog
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name = "blog"),
    #los parametros dinámicos <category_id> q pasamos por el path se detectan como una cadena de caracteres 
    # con int: forzamos q se convierta a un número 
    path('category/<int:category_id>/', views.category,name = "category")
]
