function copiarCodigo(boton) {
  const contenedor = boton.closest(".code-wrapper");
  const codigo = contenedor.querySelector("code").innerText;

  navigator.clipboard.writeText(codigo).then(() => {
    const textoOriginal = boton.innerText;
    boton.innerText = "Copiado!";
    setTimeout(() => {
      boton.innerText = textoOriginal;
    }, 2000);
  }).catch(err => {
    console.error("Error al copiar el código:", err);
  });
}