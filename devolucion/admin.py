from django.contrib import admin
from .models import doc_belnu,doc_Nacion,ExcelFileUpload
from hop.models import Hop,Empleados, Moviles,Tipo_Viaje

# Register your models here.
admin.site.register(doc_belnu)
admin.site.register(doc_Nacion)
admin.site.register(ExcelFileUpload)
admin.site.register(Hop)
admin.site.register(Empleados)
admin.site.register(Tipo_Viaje)
admin.site.register(Moviles)