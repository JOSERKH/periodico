from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('cerrar/', views.cerrar_sesion, name='cerrar_sesion'),  # 👈 nueva línea

]
