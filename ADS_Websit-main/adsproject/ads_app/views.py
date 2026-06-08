from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .models import (
    PostDisciplina, PostMonitoria, PostNoticia,
    Evento, Extensao, Projeto, Documentacao
)


class BaseView(TemplateView):
    template_name = 'base.html'


# ── HOME ──────────────────────────────────────────────────────────────────────
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimas_noticias'] = PostNoticia.objects.order_by('-data_publicacao')[:3]
        return context


# ── DISCIPLINAS ───────────────────────────────────────────────────────────────
class DisciplinasView(ListView):
    model = PostDisciplina
    template_name = 'disciplinas.html'
    context_object_name = 'disciplinas'
    ordering = ['periodo', 'nome_disciplina']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['periodos'] = range(1, 6)
        return context


# ── EXTENSÕES ─────────────────────────────────────────────────────────────────
class ExtensoesView(TemplateView):
    template_name = 'extensoes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extensoes_atuais'] = Extensao.objects.filter(tipo='Atual')
        context['extensoes_futuras'] = Extensao.objects.filter(tipo='Futura')
        return context


# ── NOTÍCIAS ──────────────────────────────────────────────────────────────────
class NoticiasView(TemplateView):
    template_name = 'noticias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos'] = Evento.objects.all()
        context['noticias'] = PostNoticia.objects.all().order_by('-data_publicacao')
        return context


# ── DOCUMENTOS ────────────────────────────────────────────────────────────────
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


# ── PROJETOS ──────────────────────────────────────────────────────────────────
class ProjetosView(TemplateView):
    template_name = 'projetos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        projetos = Projeto.objects.all()

        nome = self.request.GET.get('nome')
        if nome:
            projetos = projetos.filter(nome_projeto__icontains=nome)

        ano = self.request.GET.get('ano')
        if ano:
            projetos = projetos.filter(ano=ano)

        tipo_parceria = self.request.GET.get('tipo_parceria')
        if tipo_parceria:
            projetos = projetos.filter(tipo_parceria=tipo_parceria)

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
        context['anos_disponiveis'] = (
            Projeto.objects.exclude(ano__isnull=True)
            .values_list('ano', flat=True).distinct().order_by('-ano')
        )
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


# ── MONITORIAS ────────────────────────────────────────────────────────────────
class MonitoriasView(TemplateView):
    template_name = "monitorias.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['monitorias'] = PostMonitoria.objects.all()
        return context


# ── CONTATO ───────────────────────────────────────────────────────────────────
class ContatoView(TemplateView):
    template_name = 'contato.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_enviado'] = self.request.GET.get('enviado') == '1'
        context['form_erro']    = self.request.GET.get('erro')    == '1'
        return context


def enviar_contato(request):
    if request.method == 'POST':
        nome     = request.POST.get('nome', '').strip()
        email    = request.POST.get('email', '').strip()
        mensagem = request.POST.get('mensagem', '').strip()

        if not nome or not email or '@' not in email or not mensagem:
            return redirect('/contato/?erro=1')

        # Se quiser enviar email, descomente e configure EMAIL_* no settings.py:
        # from django.core.mail import send_mail
        # send_mail(
        #     subject=f'Contato do site - {nome}',
        #     message=f'De: {nome} <{email}>\n\n{mensagem}',
        #     from_email=email,
        #     recipient_list=['coordenacao@ads.fiponline.edu.br'],
        # )

        return redirect('/contato/?enviado=1')

    return redirect('/contato/')


# ── MATRIZ CURRICULAR ─────────────────────────────────────────────────────────
def matriz_curricular(request):
    return render(request, 'matriz_curricular.html')