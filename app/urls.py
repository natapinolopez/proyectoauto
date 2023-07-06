from django.urls import path
from .views import home, contacto, inicio, servicio, acercade
from . import views
# from .views import login_view, registro, inicio_sesion, cerrar_sesion
from .views import login_view, register_view, logout_view

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name='contacto'),
    path('inicio/', inicio, name="inicio"),
    path('servicio/', servicio, name="servicio"),
    path('acercade/', acercade, name="acercade"),
    path('login/', login_view, name='login'),
    path('registro/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
