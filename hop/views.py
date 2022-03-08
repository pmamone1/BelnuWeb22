from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Hop
from .forms import HopForm

# Create your views here.

def crear_hop(request):
    form=HopForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('consultar_hop')
    return render(request, 'crear_hop.html',{'form':form})

def consultar_hop(request):
    registros=Hop.objects.all()
    return render(request, 'consulta_hop.html',{'registros':registros})

def eliminar_hop(request,id):
    registro = Hop.objects.get(id=id)
    registro.delete()
    return redirect('consultar_hop')

def editar_hop(request,id):
    registro = Hop.objects.get(id=id)
    form=HopForm(request.POST or None, request.FILES or None, instance=registro)
    if form.is_valid():
        form.save()
        return redirect('consultar_hop')
    return render(request, 'crear_hop.html',{'form':form})
