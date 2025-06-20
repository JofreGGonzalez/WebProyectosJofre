document.addEventListener('DOMContentLoaded', () => {

  // Usando jQuery para el scroll y la clase sticky
  window.addEventListener('scroll', () => {
    var scrollTop = $(window).scrollTop(); // corregido 'this' por 'window'
    if (scrollTop <= 0) {
      $(".navBar").removeClass("sticky");
    } else {
      $(".navBar").addClass("sticky");
    }
  });

  const sections = document.querySelectorAll(".sec");
  const navLi = document.querySelectorAll("#navi li");

  window.addEventListener('scroll', () => {
    let current = "";

    sections.forEach((section) => {
      const sectionTop = section.offsetTop;
      if (window.scrollY >= sectionTop - 130) {
        current = section.getAttribute("id");
      }
    });

    navLi.forEach((li) => {
      li.classList.remove("activebar");
      if (li.classList.contains(current)) {
        li.classList.add("activebar");
      }
    });
  });

});