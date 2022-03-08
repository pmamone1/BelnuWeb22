from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('home/', views.inicio, name='inicio'),
    path('devolucion/crear/', views.crear, name='crear'),
    path('devolucion/editar/', views.editar, name='editar'),
    path('devolucion/consultar/', views.consultar, name='consultar'),
    path('devolucion/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('devolucion/editar/<int:id>', views.editar, name='editar'),
]
