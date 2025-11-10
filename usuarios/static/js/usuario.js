document.addEventListener("DOMContentLoaded", () => {
    const registroForm = document.getElementById("registroForm");
    const loginForm = document.getElementById("loginForm");

    if (registroForm) {
        registroForm.addEventListener("submit", (e) => {
            const pass1 = document.getElementById("password1").value;
            const pass2 = document.getElementById("password2").value;
            if (pass1 !== pass2) {
                e.preventDefault();
                alert("Las contraseñas no coinciden.");
            }
        });
    }

    if (loginForm) {
        loginForm.addEventListener("submit", (e) => {
            const email = document.getElementById("email").value.trim();
            if (!email.includes("@")) {
                e.preventDefault();
                alert("Por favor ingresa un correo válido.");
            }
        });
    }
});
