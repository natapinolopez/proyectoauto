from django.urls import path
from .views import home, contacto, inicio, servicio, acercade, agregar_al_carrito, ver_carrito, eliminar_del_carrito
from . import views
# from .views import login_view, registro, inicio_sesion, cerrar_sesion
from .views import login_view, register_view, logout_view

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name='contacto'),
    path('inicio/', inicio, name="inicio"),
    path('servicio/', servicio, name="servicio"),
    path('agregar-al-carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', ver_carrito, name='carrito'),
    path('eliminar-del-carrito/<int:producto_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('acercade/', acercade, name="acercade"),
    path('login/', login_view, name='login'),
    path('registro/', views.register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
