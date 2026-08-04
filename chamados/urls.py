from django.urls import path
from chamados import views


urlpatterns = [
    path('criar_chamado/', views.criar_chamado, name="form_criar_chamado"),

]