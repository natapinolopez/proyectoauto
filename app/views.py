from django.shortcuts import render, redirect
from .models import Producto, Contacto
from .forms import ContactoForm, ProductoForm
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

# def servicio(request):
#     productos = Producto.objects.all()
#     data={
#         'carts' : productos
#     }
#     return render(request, 'app/servicio.html',data)
def servicio(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('servicio')  # Redirecciona a la misma página después de guardar el producto

    else:
        form = ProductoForm()

    productos = Producto.objects.all()
    data = {
        'carts': productos,
        'form': form
    }
    return render(request, 'app/servicio.html', data)
