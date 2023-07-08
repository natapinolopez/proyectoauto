from django.shortcuts import render, redirect
from .models import Producto, Contacto, Cuenta, CuentaManager
from .forms import ContactoForm, ProductoForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm, AutenticarForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
@csrf_protect

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
def agregar_al_carrito(request, producto_id):
    
    producto = Producto.objects.get(pk=producto_id)

    # Verificar si el carrito de compras ya existe en la sesión
    if 'carrito' not in request.session:
        request.session['carrito'] = []

    # Agregar el producto al carrito de compras
    carrito = request.session['carrito']
    carrito.append(producto_id)
    request.session.modified = True  

    return redirect('carrito')

def ver_carrito(request):
    carrito_ids = request.session.get('carrito', [])
    carrito = Producto.objects.filter(pk__in=carrito_ids)
    total = carrito.aggregate(total=Sum('precio'))['total'] or 0

    return render(request, 'app/carrito.html', {'carrito': carrito, 'total': total})

def eliminar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('carrito')  

    return render(request, 'app/confirmar_eliminar.html', {'product': producto})

def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # No guardar el usuario todavía
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)  # Establecer la contraseña cifrada
            user.save()  # Guardar el usuario en la base de datos
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login')  # Redirigir a la página de login
    else:
        form = RegistroForm()

    return render(request, 'registro/registro.html', {'form': form})


def global_context(request):
    user = request.user
    return {'user': user}


@login_required
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email= form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Correo electrónico o contraseña incorrectos')
    else:
        form = LoginForm()

    return render(request, 'registro/login.html', {'form': form})




def csrf_failure_view(request, reason=""):
    return render(request, 'csrf_failure.html', {'reason': reason}, status=403)

def logout_view(request):
    logout(request)
    return redirect('login')  





















# def login_view(request):
#     return render(request, 'registro/login.html')

# def registro(request):
#     if request.method == 'POST':
#         form = RegistroForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             # Crear un nuevo objeto Cuenta
#             cuenta = CuentaManager.create_user(email=email, password=password, nombre='Nombre')

#             # Guardar el objeto en la base de datos
#             cuenta.save()

            
            
#             return redirect('/login')
#     else:
#         form = RegistroForm()
#     return render(request, 'registro/registro.html', {'form': form})



# def inicio_sesion(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
            
#             try:
#                 # Autenticar al usuario
#                 usuario = Cuenta.objects.get(email=email)
#                 if usuario.check_password(password):
#                     # Iniciar sesión
#                     login(request, usuario)
#                     return redirect('/')
#                 else:
#                     form.add_error(None, "El email o contraseña son incorrectos")
#             except Cuenta.DoesNotExist:
#                 form.add_error(None, "El email o contraseña son incorrectos")
#     else:
#         form = LoginForm()

#     context = {'form': form}
    
#     return render(request, 'registro/login.html', context)


# def cerrar_sesion(request):
#     logout(request)
#     return redirect('/')






