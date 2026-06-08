from django.contrib import admin
from .models import (
    PostNoticia, PostDisciplina, PostMonitoria,
    Evento, Extensao, Projeto, Documentacao
)

@admin.register(PostNoticia)
class PostNoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo_noticia', 'data_publicacao', 'descricao_resumida')
    list_filter = ('data_publicacao',)
    search_fields = ('titulo_noticia',)
    ordering = ('-data_publicacao',)

@admin.register(PostDisciplina)
class PostDisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome_disciplina', 'nome_professor', 'periodo', 'tipo')
    list_filter = ('periodo', 'tipo')
    search_fields = ('nome_disciplina', 'nome_professor')

@admin.register(PostMonitoria)
class PostMonitoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo_monitoria', 'descricao_resumida')

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome_evento', 'data_evento', 'link_evento')
    ordering = ('-data_evento',)

@admin.register(Extensao)
class ExtensaoAdmin(admin.ModelAdmin):
    list_display = ('nome_extensao', 'professor', 'tipo')
    list_filter = ('tipo',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome_projeto', 'ano', 'tipo_parceria', 'tecnologia')
    list_filter = ('ano', 'tipo_parceria')
    search_fields = ('nome_projeto',)

@admin.register(Documentacao)
class DocumentacaoAdmin(admin.ModelAdmin):
    list_display = ('nome_arquivo', 'tipo')
    list_filter = ('tipo',)