from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import Hop,Empleados,Moviles,Tipo_Viaje
from .forms import HopForm

# Create your views here.

def crear_hop(request):
    form=HopForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('consultar_hop')
    choferes=Empleados.objects.filter(puesto__icontains='chofer')
    acomp=Empleados.objects.filter(puesto__icontains='acompañante')
    moviles=Moviles.objects.all()
    tipos=Tipo_Viaje.objects.all()
    valor_peon=Tipo_Viaje.objects.filter(tipo='acompañante')
    turnos=['Mañana','Tarde','Noche']
    return render(request, 'crear_hop.html',{'form':form,'choferes':choferes,'peones':acomp,'moviles':moviles,'turnos':turnos,'tipos':tipos,'valor_peon':valor_peon})

def get_valor_viaje(request):
    if request.is_ajax():
        res = None
        data = request.POST.get('tipo')
        print("PABLOOOO")
        print(data)
        qs=Tipo_Viaje.objects.filter(tipo__icontains=data)
        if len(qs) > 0 and len(data)>0:
            data=[]
            for pos in qs:
                item={
                    'pk':pos.id,
                    'tipo':pos.tipo,
                    'valor':pos.valor_viaje
                }
                data.append(item)
            res=data
        else:
            res=None
        return JsonResponse({'data':res})
    return JsonResponse({})

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
