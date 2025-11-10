from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Noticia
from .forms import NoticiaForm

@login_required
def lista_noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, 'noticias/lista_noticias.html', {'noticias': noticias})

@login_required
def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.save()
            return redirect('lista_noticias')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/crear.html', {'form': form})
