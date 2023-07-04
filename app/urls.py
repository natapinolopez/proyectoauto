from django.urls import path
from .views import home, contacto, inicio, servicio, acercade
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', views.contacto, name='contacto'),
    path('inicio/', inicio, name="inicio"),
    path('servicio/', servicio, name="servicio"),
    path('acercade/', acercade, name="acercade"),
    
]
