from django.urls import path
from .views import (
    IndexView, DocumentosView, DisciplinasView, NoticiasView,
    ProjetosView, ExtensoesView, MonitoriasView,
    ContatoView, enviar_contato, projeto_detalhes, matriz_curricular
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('documentos/', DocumentosView.as_view(), name='documentos'),
    path('disciplinas/', DisciplinasView.as_view(), name='disciplinas'),
    path('noticias/', NoticiasView.as_view(), name='noticias'),
    path('projetos/', ProjetosView.as_view(), name='projetos'),
    path('projetos/<int:projeto_id>/detalhes/', projeto_detalhes, name='projeto_detalhes'),
    path('extensoes/', ExtensoesView.as_view(), name='extensoes'),
    path('monitorias/', MonitoriasView.as_view(), name='monitorias'),
    path('matriz-curricular/', matriz_curricular, name='matriz_curricular'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('contato/enviar/', enviar_contato, name='enviar_contato'),
]