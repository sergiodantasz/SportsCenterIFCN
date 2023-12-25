function destacarPaginaAtualBarraNavegacao() {
  let url = window.location.pathname;
  let nomePaginaAtual;
  if (url == '/') {
    nomePaginaAtual = 'inicio';
  } else {
    nomePaginaAtual = url.split('/')[1];
  }
  let opcaoBarraNavegacao = document.getElementById(nomePaginaAtual);
  if (opcaoBarraNavegacao) {
    opcaoBarraNavegacao.classList.add('pagina-atual');
  }
}

function atualizarAlturaRodape() {
  let rodape = document.getElementById('rodape');
  let altura = rodape.getBoundingClientRect().height;
  rodape.style.bottom = -altura + 'px';
}

window.addEventListener('resize', atualizarAlturaRodape);

destacarPaginaAtualBarraNavegacao();
atualizarAlturaRodape();
