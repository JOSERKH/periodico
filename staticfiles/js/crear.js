document.addEventListener('DOMContentLoaded', function() {
    const inputImagen = document.getElementById('id_imagen');
    const preview = document.getElementById('previewImage');

    // Vista previa de imagen
    if (inputImagen) {
        inputImagen.addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = e => {
                    preview.src = e.target.result;
                    preview.style.display = 'block';
                };
                reader.readAsDataURL(file);
            } else {
                preview.style.display = 'none';
            }
        });
    }

    // Validación básica del formulario
    const form = document.getElementById('crearNoticiaForm');
    if (form) {
        form.addEventListener('submit', function(e) {
            const titulo = document.getElementById('id_titulo').value.trim();
            const contenido = document.getElementById('id_contenido').value.trim();

            if (!titulo || !contenido) {
                e.preventDefault();
                alert('Por favor, completa todos los campos obligatorios.');
            }
        });
    }
});
