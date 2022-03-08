from django.db import models
from computed_property import ComputedTextField


# Create your models here.
class doc_belnu(models.Model):
    id=models.AutoField(primary_key=True)
    agente=models.CharField(max_length=100,verbose_name='Agente',null=True,default="500-cordoba")
    movimiento=models.CharField(max_length=100,verbose_name='Movimiento')
    codigo=models.PositiveIntegerField(verbose_name='Codigo')
    edicion=models.CharField(max_length=50, verbose_name='Edicion')
    fecha=models.DateField(verbose_name='Fecha')
    titulo=models.CharField(max_length=100,verbose_name='Titulo')
    cantidad=models.IntegerField(verbose_name='Cantidad')
    precio=models.DecimalField(max_digits=18,decimal_places=2,verbose_name='Precio')
    importe=models.DecimalField(max_digits=18,decimal_places=2,verbose_name='Importe')
    pvp=models.DecimalField(max_digits=18,decimal_places=2,verbose_name='PVP')
    proveedor=models.CharField(max_length=100,verbose_name='Proveedor',default="la nacion")
    estado=models.CharField(max_length=100,verbose_name='Estado',null=True,default="pendiente")
    doc_ln_asoc=models.CharField(max_length=100,verbose_name='Doc_LN_Asociados',null=True,blank=True)
    cantidad_ln=models.IntegerField(verbose_name='Cantidad_LN',null=True,blank=True)
    importe_ln=models.DecimalField(max_digits=18,decimal_places=2,verbose_name='Importe_LN',null=True,blank=True)
    diferencia_cant=models.IntegerField(verbose_name='Diferencia_Cantidad',null=True,blank=True)
    diferencia_importe=models.DecimalField(max_digits=18,decimal_places=2,verbose_name='Diferencia_Importe',null=True,blank=True)
    obs=models.TextField(max_length=150,verbose_name='Observaciones',null=True,blank=True)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'DocumentoBelnu'
        verbose_name_plural = 'DocumentosBelnu'
        ordering=['-fecha']
        
    def __str__(self):
        fila="Id= "+ str(self.id)+ ", Titulo= "+self.titulo + ", Edicion= "+self.edicion+ ", Fecha= "+str(self.fecha)
        return fila
    
class ExcelFileUpload(models.Model):
    excel_file_upload = models.FileField(upload_to='excel')
    
    
# Modelo de los Documentos de LN
class doc_Nacion(models.Model):
    id=models.AutoField(primary_key=True)
    agente=models.CharField(max_length=100,verbose_name='Agente',null=True,default="500-cordoba")
    tipo_doc=models.CharField(max_length=100,verbose_name='Tipo_Doc',null=True,blank=True)
    fecha=models.DateField(verbose_name='Fecha')
    fecha_vto=models.DateField(verbose_name='Fecha_Vto')
    material=models.CharField(max_length=100,verbose_name='Material',null=True,blank=True)
    titulo=models.CharField(max_length=100,verbose_name='Titulo')
    nro_doc=models.CharField(max_length=100,verbose_name='Doc_LN_Asociados',null=True,blank=True)
    movimiento=models.CharField(max_length=100,verbose_name='Movimiento')
    cantidad=models.IntegerField(verbose_name='Cantidad')
    pvp=models.DecimalField(max_digits=18,decimal_places=2,verbose_name='PVP')
    desc_cadena=models.DecimalField(max_digits=18,decimal_places=2,verbose_name='Desc_Cadena',null=True,blank=True)
    recargo=models.DecimalField(max_digits=18,decimal_places=2,verbose_name='Recargo',null=True,blank=True)
    importe=models.DecimalField(max_digits=18,decimal_places=2,verbose_name='Importe')
    
    controlado=models.CharField(max_length=25,verbose_name="Controlado",default="no")
    diferencias=models.CharField(max_length=25,verbose_name="Diferencias",default="no")
    obs=models.TextField(max_length=150,verbose_name='Observaciones',null=True,blank=True)
    
    costo=ComputedTextField(compute_from='calc_costo', verbose_name="Costo")
    edicion = ComputedTextField(compute_from='calc_edicion',verbose_name="Edicion",null=True,blank=True)
    codigo=ComputedTextField(compute_from='calc_codigo', verbose_name="Codigo",null=True,blank=True)    
    tipo_pub=ComputedTextField(compute_from='calc_tipo_pub',verbose_name="Tipo_Publicacion",null=True,blank=True)
    
    @property
    def calc_costo(self):
        print(str(self.pvp) +" "+ str(self.costo))
        resultado=((self.pvp)*(self.costo+100)/100)+self.recargo
        print(str(resultado))
        return resultado
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'DocumentoLN'
        verbose_name_plural = 'DocumentosLN'
        #ordering=['-fecha_vto']
        
    def __str__(self):
        fila="Id= "+ str(self.id)+ ", Titulo= "+self.titulo + ", Edicion= "+self.edicion
        return fila
    