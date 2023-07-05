from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import Cuenta

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





class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingresa un email válido.')

    class Meta:
        model = Cuenta
        fields = ('email', 'password1', 'password2')


class AutenticarForm(forms.ModelForm):
    password = forms.CharField(label='contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Cuenta
        fields = ['email', 'password']

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("El email o contraseña son incorrectos")


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
