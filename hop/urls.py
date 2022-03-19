from django.urls import path
from . import views


urlpatterns = [
    path('hop/crear/', views.crear_hop, name='crear_hop'),
    path('hop/consultar/', views.consultar_hop, name='consultar_hop'),
    path('hop/eliminar/<int:id>', views.eliminar_hop, name='eliminar_hop'),
    path('hop/editar/<int:id>', views.editar_hop, name='editar_hop'),
    path('hop/viajes/api/', views.hop_viajes_api, name='hop_viajes_api'),
    path('hop/tipo-viajes/api/', views.tipoViajes_api, name='tipoViajes_api'),
    path('hop/moviles/api/', views.moviles_api, name='moviles_api'),
    path('hop/empleados/api/', views.empleados_api, name='empleados_api'),
    path('hop/empleado/api/<int:id>', views.empleado_api, name='empleado_api'),
    path('hop/movil/api/<int:id>', views.movil_api, name='movil_api'),
   # path('hop/tipo-viaje/api/<int:id>', views.tipo_viaje_api, name='tipo_viaje_api'),
    path('hop/viaje/api/<int:id>', views.hop_viaje_api, name='hop_viaje_api'),
    path('hop/tipo-viaje/ajax/valor/', views.checValor, name = "checkValor"),
]
