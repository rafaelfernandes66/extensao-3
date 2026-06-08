from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse



# Create your views here.
class BaseView(TemplateView):
    template_name = 'base.html'

class IndexView(TemplateView):
    template_name = 'index.html'

class DisciplinasView(ListView):
    model = PostDisciplina
    template_name = 'disciplinas.html'
    context_object_name = 'disciplinas'
    ordering = ['periodo', 'nome_disciplina']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['periodos'] = range(1, 6)
        return context

class ExtensoesView(TemplateView):
    template_name = 'extensoes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extensoes_atuais'] = Extensao.objects.filter(tipo='Atual')
        context['extensoes_futuras'] = Extensao.objects.filter(tipo='Futura')
        return context

class NoticiasView(TemplateView):
    template_name = 'noticias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos'] = Evento.objects.all()
        context['noticias'] = PostNoticia.objects.all().order_by('-data_publicacao')
        return context

class DocumentosView(TemplateView):
    template_name = 'documentos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos'] = Evento.objects.all()
        context['requerimentos'] = Documentacao.objects.filter(tipo='Requerimento')
        context['arquivos'] = Documentacao.objects.filter(tipo='Arquivo')
        context['prouni'] = Documentacao.objects.filter(tipo='Prouni')
        context['fies'] = Documentacao.objects.filter(tipo='FIES')
        return context

class ProjetosView(TemplateView):
    template_name = 'projetos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        projetos = Projeto.objects.all()
        
        nome = self.request.GET.get('nome')
        if nome:
            projetos = projetos.filter(nome_projeto__icontains=nome)
        
        # Filtrar por ano
        ano = self.request.GET.get('ano')
        if ano:
            projetos = projetos.filter(ano=ano)
        
        # Filtrar por tipo de parceria
        tipo_parceria = self.request.GET.get('tipo_parceria')
        if tipo_parceria:
            projetos = projetos.filter(tipo_parceria=tipo_parceria)
        
        # Filtrar por tecnologia (busca parcial)
        tecnologia = self.request.GET.get('tecnologia')
        if tecnologia:
            projetos = projetos.filter(tecnologia__icontains=tecnologia)
        
        paginator = Paginator(projetos, 4)
        page = self.request.GET.get('page', 1)
        
        try:
            projetos_paginados = paginator.page(page)
        except PageNotAnInteger:
            projetos_paginados = paginator.page(1)
        except EmptyPage:
            projetos_paginados = paginator.page(paginator.num_pages)
        
        context['projetos'] = projetos_paginados
        context['page_obj'] = projetos_paginados
        
        context['anos_disponiveis'] = Projeto.objects.exclude(ano__isnull=True).values_list('ano', flat=True).distinct().order_by('-ano')
        context['tipos_parceria'] = Projeto.TIPO_PARCERIA_CHOICES
        
        return context

def projeto_detalhes(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    
    data = {
        'id': projeto.id,
        'nome_projeto': projeto.nome_projeto,
        'descricao_projeto': projeto.descricao_projeto,
        'img_projeto': projeto.img_projeto.url if projeto.img_projeto else None,
        'ano': projeto.ano,
        'tipo_parceria': projeto.get_tipo_parceria_display() if projeto.tipo_parceria else None,
        'tecnologia': projeto.tecnologia,
        'equipe': projeto.equipe,
        'repositorio_url': projeto.repositorio_url,
        'periodo_desenvolvimento': projeto.periodo_desenvolvimento,
        'descricao_ampliada': projeto.descricao_ampliada,
        'video_url': projeto.video_url,
    }
    
    return JsonResponse(data)

class MonitoriasView(TemplateView):
    template_name = "monitorias.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['monitorias'] = PostMonitoria.objects.all()
        return context
    
def matriz_curricular(request):
    return render(request, 'matriz_curricular.html')