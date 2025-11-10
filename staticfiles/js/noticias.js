// noticias.js

document.addEventListener("DOMContentLoaded", () => {
    const contenedor = document.getElementById("listaNoticias");

    // Ejemplo: mensaje en consola cuando se hace scroll
    contenedor.addEventListener("scroll", () => {
        if (contenedor.scrollTop + contenedor.clientHeight >= contenedor.scrollHeight) {
            console.log("Has llegado al final del listado de noticias 📜");
        }
    });
});
