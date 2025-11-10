from django.db import models
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='noticias')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
