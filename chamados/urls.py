from django.urls import path
from chamados import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.ChamadoListView.as_view(), name="listar_chamados"),
    path('criar_chamado/', views.ChamadoCreateView.as_view(), name="form_criar_chamado"),
    path('atualizar_status/<int:pk>/',views.atualizar_status, name="atualizar_status"),
    path('excluir_chamado/<int:pk>/',views.ChamadoDeleteView.as_view(),name="excluir_chamado"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='chamados/login.html'),name='login' )
]