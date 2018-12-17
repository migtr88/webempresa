from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.
def contact(request):
    contact_form = ContactForm()
    #Para recuperar el formulario hemos de detectar q sea una petición POST en la q se envien datos 
    if request.method == "POST":
        #rellenamos el objeto formulario con los campos que se mandan en la petición POST
        contact_form = ContactForm(data= request.POST) 
        #Comprobamos q el formulario sea valido, campos rellenos correctamente
        if contact_form.is_valid():
            #Si es valido recuperamos los campos 
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #Enviamos el correo 
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",#asunto
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),#cuerpo le pasamos los datos para formar el cuerpo del correo
                "no-contestar@inbox.mailtrap.io",#email_origen
                ["migtr1988@gmail.com"],#email_destino, lista con todos los emails a los que se quiere enviar el mensaje
                reply_to = [email],#email al q se responderá
            )   
                #Mandamos el mail, lo ponemos en un bucle Try por si salta aun error
            try:
                email.send()
                #redireccionamos a contact con un get si todo va bien, mandándole un ok
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?failEmail")     
            
            
    return render(request, 'contact/contact.html',{'form':contact_form})