# Projeto Site Institucional - Curso de Análise e Desenvolvimento de Sistemas (ADS)

## 📚 Descrição

Este é um site institucional desenvolvido como projeto para o curso de Análise e Desenvolvimento de Sistemas (ADS).  
O sistema foi construído utilizando **Django** (monolítico), com recursos de **JavaScript** e **Bootstrap** para proporcionar uma interface moderna e responsiva.

## 🚀 Funcionalidades

- Página inicial institucional
- Apresentação do curso e equipe
- Seção de notícias e novidades
- Formulário de contato
- Área para divulgação de eventos
- Design responsivo (compatível com dispositivos móveis)

## 🛠️ Tecnologias Utilizadas

- [Django](https://www.djangoproject.com/) (backend e template engine)
- [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) (interatividade)
- [Bootstrap](https://getbootstrap.com/) (estilização e responsividade)
- HTML5 e CSS3

## 📁 Estrutura de Diretórios

```bash

adsproject/
├── static/
├── templates/
├── media/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── adsproject/ # Configuração do Django (settings, urls, wsgi)
│
├── ads_app/ # Aplicação principal do projeto
│ ├── migrations/ 
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ └── views.py
│
└── ...

```

## ⚙️ Como rodar o projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

   ```
2. **Crie e ative o ambiente virtual**   
   ```bash
    
    python -m venv venv
    # No Windows
    venv\Scripts\activate
    # No Linux/Mac
    source venv/bin/activate
   
   ```
3. **Instale as dependências**

   ```bash

   pip install -r requirements.txt
   # Aplique as migrações
   python manage.py migrate
   # Execute o servidor
   python manage.py runserver

    ```
4. *Acesse no navegador*
http://localhost:8000   
   
   
## 🤝 Contribuição
Fique à vontade para sugerir melhorias ou reportar bugs abrindo uma issue ou enviando um pull request!

## Histórico de Colaboradores

### Autores:
- Carlos Daniel
- Gabriel de Oliveira Silva
- Guilherme Medeiros da Silva
- Pâmella Maria
- Pedro Henrique de Lucema

### Equipe 2026.2
- Rafael Fernandes
- Anderson Silva
- João victor

Projeto desenvolvido para o Curso de Análise e Desenvolvimento de Sistemas da Unifip.
