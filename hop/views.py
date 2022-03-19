from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import Hop,Empleados,Moviles,Tipo_Viaje
from .forms import HopForm
from django.core import serializers
from rest_framework.parsers import JSONParser
from .serializers import HopSerializer,TipoViajeSerializer,EmpleadosSerializer,MovilesSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import simplejson

###############################################################################################################        
##############    API'S  ################
###############################################################################################################



@api_view(['GET','POST'])
def hop_viajes_api(request):
  if request.method=="GET":
      datos=Hop.objects.all()
      serializer=HopSerializer(datos,many=True)
      return Response(serializer.data)
  
  elif request.method=="POST":
      serializer=HopSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def tipoViajes_api(request):
  if request.method=="GET":
      datos=Tipo_Viaje.objects.all()
      serializer=TipoViajeSerializer(datos,many=True)
      return Response(serializer.data)
  elif request.method=="POST":
      serializer=TipoViajeSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def moviles_api(request):
    if request.method=="GET":
        datos=Moviles.objects.all()
        serializer=MovilesSerializer(datos,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=MovilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def empleados_api(request):
    if request.method=="GET":
        datos=Empleados.objects.all()
        serializer=EmpleadosSerializer(datos,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=EmpleadosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def empleado_api(request,id):
    try:
        Empleado=Empleados.objects.get(id=id)
    except Empleados.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serializer=EmpleadosSerializer(Empleado)
        return Response(serializer.data)
    
    elif request.method=="PUT":
        serializer=EmpleadosSerializer(Empleado,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    
    elif request.method=="DELETE":
        Empleado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def movil_api(request,id):
    try:
        Movil=Moviles.objects.get(id=id)
    except Moviles.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serializer=MovilesSerializer(Movil)
        return Response(serializer.data)
    
    elif request.method=="PUT":
        serializer=MovilesSerializer(Movil,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    
    elif request.method=="DELETE":
        Movil.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def tipo_viaje_api(request,id):
    try:
        Tipo=Tipo_Viaje.objects.get(id=id)
    except Tipo_Viaje.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serializer=TipoViajeSerializer(Tipo)
        return Response(serializer.data)
    
    elif request.method=="PUT":
        serializer=TipoViajeSerializer(Tipo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    
    elif request.method=="DELETE":
        Tipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','PUT','DELETE'])
def hop_viaje_api(request,id):
    try:
        hop=Hop.objects.get(id=id)
    except Hop.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serializer=HopSerializer(hop)
        return Response(serializer.data)
    
    elif request.method=="PUT":
        serializer=HopSerializer(hop,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    
    elif request.method=="DELETE":
        hop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###############################################################################################################        
##############   FIN  DE  API'S  ################
###############################################################################################################

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


def checValor(request):
    # request should be ajax and method should be GET.
    if request.is_ajax():
        # get the nick name from the client side.
        valor = request.GET.get("#tipo", None)
        # check for the nick name in the database.
        if Tipo_Viaje.objects.filter(tipo__icontains=valor).exists():
            # if nick_name found return not valid new friend
            valor=Tipo_Viaje.objects.filter(tipo__icontains=valor)
            print(valor + " " + valor)
            return JsonResponse({"valor":valor.valor_viaje}, status = 200)
        else:
            # if nick_name not found, then user can create a new friend.
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({"valid":False}, status = 400)

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
