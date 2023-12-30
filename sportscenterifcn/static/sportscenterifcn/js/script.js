let menuMobile = document.querySelector('.barra-navegacao .menu-mobile');
let menu = document.querySelector('.barra-navegacao .menu');

menuMobile.addEventListener('click', () => {
  menuMobile.classList.toggle('active');
  menu.classList.toggle('active');
})

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

function atualizarDimensoesRodape() {
  let rodape = document.getElementById('rodape');
  let altura = rodape.getBoundingClientRect().height;
  rodape.style.bottom = -altura + 'px';
  let larguraPagina = document.documentElement.clientWidth;
  rodape.style.width = larguraPagina + 'px';
}

window.addEventListener('resize', atualizarDimensoesRodape);

destacarPaginaAtualBarraNavegacao();
atualizarDimensoesRodape();
