from django.urls import path
from chamados import views


urlpatterns = [
    path('',views.ChamadoListView.as_view(), name="listar_chamados"),
    path('criar_chamado/', views.ChamadoCreateView.as_view(), name="form_criar_chamado"),
    path('atualizar_status/<int:pk>/',views.atualizar_status, name="atualizar_status"),
    path('excluir_chamado/<int:pk>/',views.ChamadoDeleteView.as_view(),name="excluir_chamado")
]