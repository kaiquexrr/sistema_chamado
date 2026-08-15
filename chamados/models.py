from django.db import models

# Create your models here.

PRIORIDADE_CHOICES = (
    ('URGENTE','URGENTE'),
    ('MEDIA', 'MEDIA'),
    ('BAIXA','BAIXA')
)

TIPO_CHOICES = (
    ('HARDWARE','HARDWARE'),
    ('SOFTWARE','SOFTWARE')
)


class Chamado(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    prioridade = models.CharField(max_length=7,choices=PRIORIDADE_CHOICES)
    tipo = models.CharField(max_length=8,choices=TIPO_CHOICES)
    data_criacao = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    resolvido = models.BooleanField(default=False)
    def __str__(self):
        return self.titulo

    