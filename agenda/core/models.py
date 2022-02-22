from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    dt_evento = models.DateTimeField(verbose_name='Data do Evento')     # verbose_name edita o nome do campo
    dt_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # acresenta o campo usuario, e posibilita ao excluir o usuario, deletar  todos os seus eventos

    class Meta:
        db_table = 'evento'  # determinando que a tabela se chame 'evento'

    def __str__(self):
        return self.titulo

    def get_dt_evento(self):
        return self.dt_evento.strftime('%d/%m/%y %H:%M')