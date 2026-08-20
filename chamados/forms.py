from django import forms
from .models import Chamado


class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['titulo', 'descricao', 'prioridade', 'tipo', 'email', 'resolvido']


    def form_valid(self,form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)