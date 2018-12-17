from django import forms

class ContactForm(forms.Form):
    #Con widget extendemos unos atributos para darle forma al campo del formulario 
    name =forms.CharField(label = "Nombre", required = True,  widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Escribe tu nombre'}
    ), min_length = 3, max_length = 100)
    email=forms.EmailField(label = "Correo electrónico", required = True, widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'Escribe tu email'} 
    ),min_length = 10, max_length = 100)
    #widget le da al campo aspecto diferente aunq siga siendo un cmapo de texto
    content = forms.CharField(label = "Contenido", required = True, widget= forms.Textarea( 
        attrs={'class':'form-control','rows':3, 'placeholder':'Escribe tu mensaje'}
    ) ,min_length = 15, max_length = 300 )