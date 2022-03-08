from unicodedata import decimal
from django.db import models
from computed_property import ComputedTextField

_turnos=[('Mañana','Mañana'),('Tarde','Tarde'),('Noche','Noche')]

# Create your models here.
class Hop(models.Model):
    id=models.AutoField(primary_key=True)
    fecha=models.DateField(auto_now=False, auto_now_add=False,verbose_name="Fecha:")
    turno=models.CharField(max_length=30,choices=_turnos,verbose_name="Turno:",default="Mañana")
    chofer=models.CharField(max_length=60,verbose_name="Chofer:")
    movil=models.CharField(max_length=30,verbose_name="Movil:")
    acomp=models.CharField(max_length=60,verbose_name="Acompañante:",null=True,blank=True)
    tipo=models.CharField(max_length=30,verbose_name="Tipo Viaje:",choices=[('Camion Drop Off','Camion Drop Off'),('Sprinter Drop Off','Sprinter Drop Off'),('Sprinter Pick Up','Sprinter Pick Up')])
    cant_viajes=models.PositiveIntegerField(default="1",verbose_name="Cantidad de Viajes:")
    cant_acomp=models.PositiveIntegerField(default="0",verbose_name="Cantidad de Acompañantes:")
    cant_paquetes=models.PositiveIntegerField(default="0",verbose_name="Cantidad de Paquetes:")
    tarifa_camion=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Tarifa Camion:",default=0)
    tarifa_acomp=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Tarifa Acompañante:",default=0)
    obs=models.TextField(max_length=500,verbose_name="Observaciones:",blank=True)
 
    importe=ComputedTextField(compute_from='_importe', verbose_name="Importe:",null=True,blank=True)
    imp_final = ComputedTextField(compute_from='_imp_final',verbose_name="Importe Final:",null=True,blank=True)
    
    @property
    def _importe(self):
        print(str(self.tarifa_camion) +"+"+ str(self.tarifa_acomp))
        resultado=(float(self.tarifa_camion)*(self.cant_viajes))+float((self.tarifa_acomp*self.cant_acomp))
        print(str(resultado))
        return resultado
    
    @property
    def _imp_final(self):
        resultado=(float(self.importe)*1.21)
        return resultado
    

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Hop'
        verbose_name_plural = 'Hops'
        ordering=['-fecha']
        
    def __str__(self):
        fila="Id= "+ str(self.id)+ ", Chofer= "+self.chofer + ", importe= "+self.imp_final
        return fila

class Empleados(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=60,verbose_name="Nombre:")
    apellido=models.CharField(max_length=60,verbose_name="Apellido:")
    puesto=models.CharField(max_length=60,verbose_name="Puesto:",choices=[('Chofer','Chofer'),('Acompañante','Acompañante')])
    
    def __str__(self):
        fila="Nombre= "+ str(self.nombre)+ ", Apellido= "+self.apellido + ", puesto= "+self.puesto
        return fila


class Tipo_Viaje(models.Model):
    id=models.AutoField(primary_key=True)
    tipo=models.CharField(max_length=60,verbose_name="Tipo de Viaje:",choices=[('Camion Drop Off','Camion Drop Off'),('Sprinter Drop Off','Sprinter Drop Off'),('Sprinter Pick Up','Sprinter Pick Up')],unique=True)
    valor_viaje=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Valor del Viaje:",default=0)
    
    def __str__(self):
        fila="Tipo= "+ self.tipo + ", Valor = $ "+ str(self.valor_viaje)
        return fila
    
class ExcelFileUpload(models.Model):
    excel_file_upload = models.FileField(upload_to='excel')

class Moviles(models.Model):
    id=models.IntegerField(primary_key=True)
    Numero=models.PositiveIntegerField(verbose_name="Numero Movil:",blank=True,null=True)
    