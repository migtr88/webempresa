from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html',{'posts':posts})

#Vista para las categorías 
def category(request, category_id):
    #Controlamos el error 404 con la funcion
    category = get_object_or_404(Category,id = category_id)
   
    return render(request, 'blog/category.html',{'category': category})