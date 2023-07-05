from django.urls import path
from .views import home, contacto, inicio, servicio, acercade
from . import views
from .views import login_view, registro, inicio_sesion, cerrar_sesion


urlpatterns = [
    path('', home, name="home"),
    path('contacto/', views.contacto, name='contacto'),
    path('inicio/', inicio, name="inicio"),
    path('servicio/', servicio, name="servicio"),
    path('acercade/', acercade, name="acercade"),
    path('login/', login_view, name='login'),
    path('registro/', registro, name='registro'),
    path('inicio_sesion/', inicio_sesion, name='inicio_sesion'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
]
