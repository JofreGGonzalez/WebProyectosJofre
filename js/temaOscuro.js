document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('themeToggle');
  const body = document.body;

  // ⬅️ Restaurar preferencia al cargar
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'light') {
    body.classList.add('light-mode');
  }

  function updateIcon() {
    const isLight = body.classList.contains('light-mode');
    toggleBtn.textContent = isLight ? '☀️' : '🌑';
  }

  toggleBtn.addEventListener('click', () => {
    body.classList.toggle('light-mode');

    // ⬅️ Guardar preferencia
    const isLight = body.classList.contains('light-mode');
    localStorage.setItem('theme', isLight ? 'light' : 'dark');

    updateIcon();
  });

  updateIcon();
});