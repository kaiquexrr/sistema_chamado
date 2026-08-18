from django.shortcuts import render
from .models import Chamado
from .forms import ChamadoForm
from django.shortcuts import get_object_or_404,redirect
from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Create your views here.



class ChamadoListView(ListView):
    model = Chamado
    template_name = 'chamados/listar_chamados.html'
    context_object_name = 'chamados'

class ChamadoCreateView(CreateView):
    model = Chamado
    form_class = ChamadoForm
    template_name = 'chamados/formulario_modelform.html'
    success_url = reverse_lazy("listar_chamados")



def atualizar_status(request, pk):
    chamado = get_object_or_404(Chamado, id=pk)

    if request.method == 'POST':
        chamado.resolvido = 'resolvido' in request.POST
        chamado.save()

        return redirect('listar_chamados')

    contexto = {
        'atualizar': chamado
    }

    return render(request, 'chamados/atualizar_status.html', contexto)



class ChamadoDeleteView(DeleteView):
    model = Chamado
    template_name = 'chamados/chamado_confirm_delete.html'
    success_url = reverse_lazy("listar_chamados")
