function animatePath(id) {
  const el = document.getElementById(id);
  const len = el.getTotalLength();
  const visibleLength = len * 0.14;
  el.style.strokeDasharray = `${visibleLength} ${len}`;
  el.style.strokeDashoffset = "0";
  el.style.animation = `traceLoop 2.1s linear infinite`;
}

// Esperar que el DOM esté listo
window.addEventListener("DOMContentLoaded", () => {
  //animatePath("light-sword");
  //animatePath("light-rock");

  animatePath("light-img");
});


