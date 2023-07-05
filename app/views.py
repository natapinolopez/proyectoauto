from django.shortcuts import render, redirect
from .models import Producto, Contacto, Cuenta, CuentaManager
from .forms import ContactoForm, ProductoForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm, AutenticarForm, LoginForm
# Create your views here.

def home(request):
    return render(request, 'app/home.html')


def contacto(request):
    data ={
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="contacto guardado"
        else:
            data["form"] = formulario
    
    return render(request, 'app/contacto.html',data)

def acercade(request):
    return render(request, 'app/acercade.html')

def inicio(request):
    return render(request, 'app/inicio.html')

def servicio(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('servicio')  
    else:
        form = ProductoForm()

    productos = Producto.objects.all()
    data = {
        'carts': productos,
        'form': form
    }
    return render(request, 'app/servicio.html', data)


def login_view(request):
    return render(request, 'registro/login.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            # Crear un nuevo objeto Cuenta
            cuenta = CuentaManager.create_user(email=email, password=password, nombre='Nombre')

            # Guardar el objeto en la base de datos
            cuenta.save()

            
            
            return redirect('/login')
    else:
        form = RegistroForm()
    return render(request, 'registro/registro.html', {'form': form})



def inicio_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                # Autenticar al usuario
                usuario = Cuenta.objects.get(email=email)
                if usuario.check_password(password):
                    # Iniciar sesión
                    login(request, usuario)
                    return redirect('/')
                else:
                    form.add_error(None, "El email o contraseña son incorrectos")
            except Cuenta.DoesNotExist:
                form.add_error(None, "El email o contraseña son incorrectos")
    else:
        form = LoginForm()

    context = {'form': form}
    
    return render(request, 'registro/login.html', context)


def cerrar_sesion(request):
    logout(request)
    return redirect('/')






