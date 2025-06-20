document.addEventListener("DOMContentLoaded", () => {
    const titulos = document.querySelectorAll(".seccion-titulo");

    titulos.forEach(titulo => {
      titulo.addEventListener("click", () => {
        const seccion = titulo.parentElement;
        seccion.classList.toggle("mostrar");
      });
    });
  });
  