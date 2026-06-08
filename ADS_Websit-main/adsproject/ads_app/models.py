from django.db import models
from django.utils.html import strip_tags

# Create your models here.
class PostDisciplina(models.Model):
    TIPO_CHOICES = [
        ('OBR', 'Obrigatória'),
        ('NOB', 'Não obrigatória'),
    ]
    id = models.AutoField(primary_key=True)
    nome_professor = models.CharField(max_length=100)
    nome_disciplina = models.CharField(max_length=100)
    img_professor = models.FileField(upload_to='professores/')
    periodo = models.IntegerField()
    descricao = models.TextField(blank=True, null=True)
    carga_horaria = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=3, choices=TIPO_CHOICES, default="OBR")
    ementa = models.FileField(upload_to='ementas/', blank=True, null=True)

    def _str_(self):
        return self.nome_professor + ' - ' + self.nome_disciplina

class PostMonitoria(models.Model):
    id = models.AutoField(primary_key=True)
    titulo_monitoria = models.CharField(max_length=200)
    descricao_monitoria = models.TextField()
    img_monitoria = models.FileField(upload_to='monitorias/')

    def descricao_resumida(self, num_caracteres = 50):
        descricao_sem_tags = strip_tags(self.descricao_monitoria)
        if len(descricao_sem_tags) > num_caracteres:
            return descricao_sem_tags[:num_caracteres] + '...'
        else:
            return descricao_sem_tags

    descricao_resumida.short_description = "Descrição resumida"

    def _str_(self):
        return self.titulo_monitoria

class Evento(models.Model):
    nome_evento = models.CharField(max_length=200)
    link_evento = models.URLField(max_length=300)
    data_evento = models.DateField(blank=True, null=True)

    def _str_(self):
        return self.nome_evento
class PostNoticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo_noticia = models.CharField(max_length=200)
    descricao_noticia = models.TextField()
    img_noticia = models.FileField(upload_to='noticias/')
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def descricao_resumida(self, num_caracteres=50):
        descricao_sem_tags = strip_tags(self.descricao_noticia)
        if len(descricao_sem_tags) > num_caracteres:
            return descricao_sem_tags[:num_caracteres] + '...'
        else:
            return descricao_sem_tags

    descricao_resumida.short_description = "Descrição resumida"

    def _str_(self):
        return self.titulo_noticia

class Extensao(models.Model):
    TIPO_EXTENSAO_CHOICES = (
        ('Atual', 'Atual'),
        ('Futura', 'Futura'),
    )

    nome_extensao = models.CharField(max_length=200)
    professor = models.CharField(max_length=200)
    assunto = models.CharField(max_length=500)
    tipo = models.CharField(max_length=10, choices=TIPO_EXTENSAO_CHOICES, default='Atual')

    def _str_(self):
        return f"{self.nome_extensao} - {self.professor}"

class Projeto(models.Model):
    TIPO_PARCERIA_CHOICES = [
        ('Parceria com Alunos', 'Parceria com Alunos'),
        ('Coordenação', 'Coordenação'),
        ('Empresa', 'Empresa'),
        ('Outro', 'Outro'),
    ]
    
    nome_projeto = models.CharField(max_length=200)
    descricao_projeto = models.TextField()
    img_projeto = models.FileField(upload_to='projetos/', blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    tipo_parceria = models.CharField(max_length=50, choices=TIPO_PARCERIA_CHOICES, blank=True, null=True)
    tecnologia = models.CharField(max_length=200, blank=True, null=True)
    equipe = models.TextField(blank=True, null=True, help_text="Membros da equipe e suas funções (um por linha)")
    repositorio_url = models.URLField(max_length=300, blank=True, null=True, help_text="Link do repositório GitHub")
    periodo_desenvolvimento = models.CharField(max_length=100, blank=True, null=True, help_text="Ex: Março a Junho de 2025")
    descricao_ampliada = models.TextField(blank=True, null=True, help_text="Descrição detalhada do projeto")
    video_url = models.URLField(max_length=300, blank=True, null=True, help_text="Link do vídeo no YouTube")

    def _str_(self):
        return self.nome_projet

class Documentacao(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('Requerimento', 'Requerimento'),
        ('Arquivo', 'Arquivo'),
        ('Prouni', 'Prouni'),
        ('FIES', 'FIES')
    ]

    nome_arquivo = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='documentacao/')
    tipo = models.CharField(max_length=20, choices=TIPO_DOCUMENTO_CHOICES, default='Arquivo')

    def _str_(self):
        return self.nome_arquivo
    