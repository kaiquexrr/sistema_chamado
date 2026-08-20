from django.shortcuts import render
from .models import Chamado
from .forms import ChamadoForm
from django.shortcuts import get_object_or_404,redirect
from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



class ChamadoListView(LoginRequiredMixin,ListView):
    model = Chamado
    template_name = 'chamados/listar_chamados.html'
    context_object_name = 'chamados'

    def get_queryset(self):
        return Chamado.objects.filter(usuario=self.request.user)


class ChamadoCreateView(LoginRequiredMixin,CreateView):
    model = Chamado
    form_class = ChamadoForm
    template_name = 'chamados/formulario_modelform.html'
    success_url = reverse_lazy("listar_chamados")

    def form_valid(self,form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)



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
