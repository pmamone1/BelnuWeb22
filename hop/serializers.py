from rest_framework import serializers
from .models import Hop, Empleados,Tipo_Viaje,Moviles


class HopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hop
        fields = '__all__'
        
class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empleados
        fields='__all__'

class TipoViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tipo_Viaje
        fields='__all__'

class MovilesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Moviles
        fields='__all__'
