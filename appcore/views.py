from django.shortcuts import render

# Create your views here.
"""
Inicio home/
Historia about(
Servicios services/
Visitanos store/
Contacto contact/
Blog blog/
Sample sample/
"""

def home(request):
    return render(request, 'appcore/home.html')

def about(request):
    return render(request, 'appcore/about.html')

def store(request):
    return render(request, 'appcore/store.html')


    
