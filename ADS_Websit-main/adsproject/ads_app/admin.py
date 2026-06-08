from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(PostDisciplina)
class PostDisciplinaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_disciplina','nome_professor', 'periodo')
    list_filter = ('nome_disciplina', 'nome_professor', 'periodo')

@admin.register(PostMonitoria)
class PostMonitoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo_monitoria')
    list_filter = ('titulo_monitoria',)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_evento', 'link_evento', 'data_evento')
    search_fields = ('nome_evento',)
    list_filter = ('data_evento',)


@admin.register(PostNoticia)
class PostNoticiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo_noticia', 'data_publicacao')
    list_filter = ('data_publicacao', 'titulo_noticia')
    search_fields = ('titulo_noticia', 'descricao_noticia')

@admin.register(Extensao)
class ExtensaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_extensao', 'professor', 'assunto', 'tipo')
    list_filter = ('tipo', 'nome_extensao', 'professor')
    search_fields = ('nome_extensao', 'professor', 'assunto')


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_projeto', 'ano', 'tipo_parceria', 'tecnologia')
    list_filter = ('ano', 'tipo_parceria', 'nome_projeto')
    search_fields = ('nome_projeto', 'descricao_projeto', 'tecnologia')
    fields = ('nome_projeto', 'descricao_projeto', 'img_projeto', 'ano', 'tipo_parceria', 'tecnologia', 
              'equipe', 'repositorio_url', 'periodo_desenvolvimento', 'descricao_ampliada', 'video_url')
    list_display_links = ('id', 'nome_projeto')
    list_editable = ()
    
    def has_change_permission(self, request, obj=None):
        return True

@admin.register(Documentacao)
class DocumentacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_arquivo', 'tipo', 'arquivo')  # Adicionei o 'tipo' para aparecer na lista
    list_filter = ('tipo',)  # Filtro lateral para escolher Requerimento ou Arquivo
    search_fields = ('nome_arquivo',)  # Permite buscar pelo nome do arquivo

