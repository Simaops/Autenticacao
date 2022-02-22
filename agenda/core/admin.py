from django.contrib import admin
from core.models import Evento  # importa o Evento primeiro

# Exibir os campos desejados da tabela no Django Admin
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'dt_evento', 'dt_criacao')
    list_filter = ('usuario', 'dt_evento')       # Insere campos Filtro  ## não esqueça da vírgula no final, aqui é obrigatória

# Register your models here.
admin.site.register(Evento, EventoAdmin)     # depois registra
