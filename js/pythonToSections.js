document.addEventListener("DOMContentLoaded", function () {
  function extraerSeccion(texto, seccion) {
    const inicio = `# --- inicio:${seccion} ---`;
    const fin = `# --- fin:${seccion} ---`;
    const regex = new RegExp(`${inicio}[\\s\\S]*?${fin}`, 'g');
    const match = texto.match(regex);
    if (!match) return 'Sección no encontrada';
    return match[0].replace(inicio, '').replace(fin, '').trim();
  }

  fetch('../files/OnePieceScraper.py')
    .then(res => res.text())
    .then(code => {
      const pasos = ['paso1', 'paso2', 'paso3', 'paso4', 'paso5', 'paso6', 'paso7', 'paso8', 'paso9', 'paso10', 'paso11', 'paso12', 'paso13', 'paso14', 'paso15', 'paso16', 'paso17', 'paso18', 'paso19']; // añade más si los tienes
      pasos.forEach(paso => {
        const el = document.getElementById(`codigo${paso.charAt(0).toUpperCase() + paso.slice(1)}`);
        if (el) {
          const seccion = extraerSeccion(code, paso);
          el.textContent = seccion;
          hljs.highlightElement(el); // aplica highlight
        }
      });
    })
    .catch(error => console.error('Error cargando el archivo:', error));
});