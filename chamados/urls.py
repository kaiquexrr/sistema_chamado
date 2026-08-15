from django.urls import path
from chamados import views


urlpatterns = [
    path('',views.listar_chamados, name="listar_chamados"),
    path('criar_chamado/', views.criar_chamado, name="form_criar_chamado"),
    path('atualizar_status/<int:id>/',views.atualizar_status, name="atualizar_status"),
    path('excluir_chamado/<int:id>/',views.excluir_chamado,name="excluir_chamado")
]