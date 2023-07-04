from django import forms
from .models import Contacto, Producto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellido', 'email', 'mensaje']
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'precio', 'imagen')