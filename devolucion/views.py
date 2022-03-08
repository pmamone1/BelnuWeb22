from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import doc_belnu,doc_Nacion,ExcelFileUpload
from .forms import Doc_belnuForm

# Create your views here.
def inicio(request):
    return render(request, 'home.html')

def crear(request):
    form=Doc_belnuForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('consultar')
    return render(request, 'crear.html',{'form':form})

def editar(request):
    return render(request, 'editar.html')

def consultar(request):
    registros=doc_belnu.objects.all()
    return render(request, 'consulta.html',{'registros':registros})

def eliminar(request,id):
    registro = doc_belnu.objects.get(id=id)
    registro.delete()
    return redirect('consultar')

def editar(request,id):
    registro = doc_belnu.objects.get(id=id)
    form=Doc_belnuForm(request.POST or None, request.FILES or None, instance=registro)
    if form.is_valid():
        form.save()
        return redirect('consultar')
    return render(request, 'crear.html',{'form':form})
