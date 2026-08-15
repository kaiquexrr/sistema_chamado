from django.contrib import admin
from .models import Chamado

# Register your models here.

@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
     list_display = ('id','titulo','prioridade')