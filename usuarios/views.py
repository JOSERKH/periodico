from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistroForm
from .models import Usuario
from .forms import LoginForm


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            print("✅ Formulario válido")
            usuario = Usuario.objects.create_user(
                email=form.cleaned_data['email'],
                nombre=form.cleaned_data['nombre'],
                password=form.cleaned_data['password1'],
                telefono=form.cleaned_data.get('telefono')
            )
            usuario.save()
            print("✅ Usuario guardado:", usuario.email)
            login(request, usuario)
            return redirect('lista_noticias')
        else:
            print("❌ Formulario inválido:", form.errors)
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # el campo del formulario
            password = form.cleaned_data.get('password')

            # ✅ Django espera 'username', aunque tu modelo use email
            usuario = authenticate(request, username=email, password=password)

            if usuario is not None:
                login(request, usuario)
                messages.success(request, f'Bienvenido {usuario.nombre}')
                return redirect('lista_noticias')  # ✅ redirige al panel de noticias
            else:
                messages.error(request, 'Correo o contraseña incorrectos.')
        else:
            messages.error(request, 'Por favor verifica tus datos.')
    else:
        form = LoginForm()

    return render(request, 'usuarios/login.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('login')
