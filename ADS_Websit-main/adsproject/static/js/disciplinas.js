document.addEventListener('DOMContentLoaded', function () {
  var disciplinaModal = document.getElementById('disciplinaModal');

  if (!disciplinaModal) return;

  disciplinaModal.addEventListener('show.bs.modal', function (event) {
  // Elemento que disparou o modal (pode ser um filho dentro do card)
  var trigger = event.relatedTarget;
  // Se não houver elemento relacionado (ex.: modal aberto por JS), abortar
  if (!trigger) return;
  // Garantir que pegamos o cartão que contém os data-attributes
  var source = trigger && typeof trigger.closest === 'function' ? trigger.closest('.disciplina-card') || trigger : trigger;

  // Ler data-attributes definidos nos cards (do elemento fonte)
  var nome = source.getAttribute('data-disciplina-nome') || '';
  var professor = source.getAttribute('data-professor-nome') || '';
  var professorImg = source.getAttribute('data-professor-img') || '';
  var descricao = source.getAttribute('data-descricao') || '';
  var carga = source.getAttribute('data-carga') || '';
  var periodo = source.getAttribute('data-periodo') || '';
  var tipo = source.getAttribute('data-tipo') || '';
  var ementa = source.getAttribute('data-ementa') || '';

  // Atualizar elementos do modal
    var elNome = document.getElementById('modal-disciplina-nome');
    var elProfessorNome = document.getElementById('modal-professor-nome');
    var elProfessorImg = document.getElementById('modal-professor-img');
    var elDescricao = document.getElementById('modal-disciplina-descricao');
    var elCarga = document.getElementById('modal-disciplina-carga');
    var elPeriodo = document.getElementById('modal-disciplina-periodo');
    var elTipo = document.getElementById('modal-disciplina-tipo');
    var elEmenta = document.getElementById('modal-disciplina-ementa');
    var ementaContainer = document.getElementById('ementa-container');

    if (elNome) elNome.textContent = nome;
    if (elProfessorNome) elProfessorNome.textContent = professor;
    if (elProfessorImg) {
      // fallback local se necessário
      elProfessorImg.src = professorImg || '/static/assets/teacher/sem-foto.png';
      elProfessorImg.alt = professor || 'Professor';
      // caso a imagem falhe ao carregar, usar fallback
      elProfessorImg.onerror = function () {
        this.onerror = null;
        this.src = '/static/assets/teacher/sem-foto.png';
      };
    }

    // Descrição (preservar quebras de linha simples)
    if (elDescricao) {
      // Escapar HTML básico para evitar XSS (os dados vêm do servidor, mas ainda assim é bom)
      elDescricao.textContent = descricao;
    }

    if (elCarga) {
      // Se o valor já contém a palavra 'horas', não duplicar
      if (carga && String(carga).toLowerCase().includes('hora')) {
        elCarga.textContent = carga;
      } else {
        elCarga.textContent = carga ? (carga + ' horas') : 'Não informada';
      }
    }

    if (elPeriodo) elPeriodo.textContent = periodo || '—';
    if (elTipo) elTipo.textContent = tipo || '—';

    if (ementa && elEmenta) {
      elEmenta.href = ementa;
      ementaContainer.style.display = 'block';
    } else if (ementaContainer) {
      ementaContainer.style.display = 'none';
    }
  });
});