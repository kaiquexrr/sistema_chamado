from django.shortcuts import render
from .models import Chamado
from .forms import ChamadoForm
from django.shortcuts import get_object_or_404

# Create your views here.

def listar_chamados(request):
    chamados = Chamado.objects.all()

    contexto = {
        'chamados':chamados
    }
    return render(request, 'chamados/listar_chamados.html',contexto)


def detalhe_chamado(request,id):
    chamado = get_object_or_404(chamado, id=id)

    contexto = {
        'chamado':chamado
    }
    return render(request,'chamados/detalhe_chamado.html',contexto)


def criar_chamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = ChamadoForm()
    contexto = {
        'form': form
    }
    
    return render(request, "chamados/formulario_modelform.html",contexto)



def atualizar_status(request,id):
    pass


def excluir_chamado(request,id):
    pass