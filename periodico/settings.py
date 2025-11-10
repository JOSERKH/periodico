"""
Django settings for periodico project.

Generado por 'django-admin startproject' usando Django 5.2.8.
"""

from pathlib import Path
import dj_database_url
import os

# === BASE DIR ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === SEGURIDAD ===
SECRET_KEY = 'django-insecure-(k$jjv(8%iypw5b*ro@$rjg3!dquo=&ug-1m&y_y3i7pq9&+w+'
DEBUG = True  # Cambia a False en producción

ALLOWED_HOSTS = ['periodico-ijfk.onrender.com', 'localhost', '127.0.0.1']

# === APLICACIONES ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Tus apps
    'usuarios',
    'noticias',
]

# === MIDDLEWARE ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise para estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# === URLS Y WSGI ===
ROOT_URLCONF = 'periodico.urls'
WSGI_APPLICATION = 'periodico.wsgi.application'

# === TEMPLATES ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# === BASE DE DATOS ===
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv(
            'DATABASE_URL',
            'sqlite:///db.sqlite3'  # fallback local
        ),
        conn_max_age=600,
        ssl_require=True
    )
}

# === VALIDACIÓN DE CONTRASEÑAS ===
AUTH_PASSWORD_VALIDATORS = []

# === INTERNACIONALIZACIÓN ===
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# === ARCHIVOS ESTÁTICOS ===
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Render servirá desde aquí

# Archivos estáticos adicionales (fuera de las apps)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# WhiteNoise: compresión y caché
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# === USUARIO PERSONALIZADO ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'usuarios.Usuario'

# === AUTENTICACIÓN ===
LOGIN_URL = '/usuarios/login/'
LOGIN_REDIRECT_URL = '/noticias/'
LOGOUT_REDIRECT_URL = '/usuarios/login/'
