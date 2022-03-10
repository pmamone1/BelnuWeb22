from django.urls import path
from . import views


urlpatterns = [
    path('hop/crear/', views.crear_hop, name='crear_hop'),
    path('hop/consultar/', views.consultar_hop, name='consultar_hop'),
    path('hop/eliminar/<int:id>', views.eliminar_hop, name='eliminar_hop'),
    path('hop/editar/<int:id>', views.editar_hop, name='editar_hop'),
    path('hop/get_valor_viaje/', views.get_valor_viaje, name='get_valor_viaje'),
]
