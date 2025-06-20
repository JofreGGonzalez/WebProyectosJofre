document.addEventListener('DOMContentLoaded', function () {
  const btn = document.getElementById('btnMenuLateral');
  const panel = document.getElementById('panelLateral');

  btn.addEventListener('click', () => {
    panel.classList.toggle('active');
  });

  // Submenús
  const submenuToggles = document.querySelectorAll('.submenu-desplegable');
  submenuToggles.forEach(toggle => {
    toggle.addEventListener('click', (e) => {
      e.preventDefault(); // Evita el salto si es un <a href="#">
      const parentLi = toggle.parentElement;
      parentLi.classList.toggle('open');
    });
  });
});