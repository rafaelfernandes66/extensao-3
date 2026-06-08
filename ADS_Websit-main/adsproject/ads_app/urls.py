
from django.urls import path
from .views import *
from ads_app import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('documentos/', DocumentosView.as_view(), name='documentos'),
    path('disciplinas/', DisciplinasView.as_view(), name='disciplinas'),
    path('noticias/', NoticiasView.as_view(), name='noticias'),
    path('projetos/', ProjetosView.as_view(), name='projetos'),
    path('projetos/<int:projeto_id>/detalhes/', projeto_detalhes, name='projeto_detalhes'),
    path('extensoes/', ExtensoesView.as_view(), name='extensoes'),
    path('monitorias/', MonitoriasView.as_view(), name='monitorias'),
    path('matriz-curricular/', views.matriz_curricular, name='matriz_curricular'),
]
