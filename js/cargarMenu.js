document.addEventListener("DOMContentLoaded", function () {
  const rutaBase = window.location.pathname.includes('/vista/') ? '../vista/nav.html' : 'vista/nav.html';

  fetch(rutaBase)
    .then(response => {
      if (!response.ok) throw new Error('Error al cargar nav.html');
      return response.text();
    })
    .then(data => {
      document.getElementById('menuLateral').innerHTML = data;

      // Ahora que el nav está en el DOM, puedes enganchar los eventos:
      const btn = document.getElementById('btnMenuLateral');
      const panel = document.getElementById('panelLateral');

      btn?.addEventListener('click', () => {
        panel?.classList.toggle('active');
      });

      const submenuToggles = document.querySelectorAll('.submenu-desplegable');
      submenuToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
          e.preventDefault();
          const parentLi = toggle.parentElement;
          parentLi.classList.toggle('open');
        });
      });
    })
    .catch(error => {
      console.error('Error al insertar el menú:', error);
    });
});