"""
Django settings for sistemakadosh project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from .email_info import EMAIL_USE_TLS,EMAIL_HOST,EMAIL_HOST_USER,EMAIL_HOST_PASSWORD,EMAIL_PORT

#EMAIL_BACKEND=EMAIL_BACKEND
EMAIL_USE_TLS=EMAIL_USE_TLS
EMAIL_HOST=EMAIL_HOST
EMAIL_HOST_USER=EMAIL_HOST_USER
EMAIL_HOST_PASSWORD=EMAIL_HOST_PASSWORD
EMAIL_PORT=EMAIL_PORT

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

MEDIA_ROOT = PROJECT_ROOT + '/archivos/'
MEDIA_URL = '/archivos/'  #put whatever you want that when url is rendered it will be /archivos_varios/imagename.jpg

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*5-fe-0ao1jir_e+4ft*r6gxrk6z13o^l@=d_zf=8%##mga7&)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #False

ALLOWED_HOSTS = ['localhost','127.0.0.1','django.kadosh','enriquesaju.pythonanywhere.com','methriks.pythonanywhere.com','www.pythonanywhere.com','www.boutiquekadosh.com'] #si el debug es falso, hay que configurar los hosts aqui
#esta parte la escribi para hacer el logueo
from django.core.urlresolvers import reverse_lazy
LOGIN_URL=reverse_lazy('login')
LOGIN_REDIRECT_URL=reverse_lazy('ingreso_mercaderia')
LOGOUT_URL=reverse_lazy('logout')

#Archivo log

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'kadoshapp': { # for your app
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': { # for all django-internal messages
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kadoshapp',
    'django_tables2',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'sistemakadosh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'sistemakadosh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'kadosh2',
        'NAME': 'methriks$kadosh2',
        #'USER': 'root',
        'USER': 'methriks',
        'PASSWORD': 'hola1234',
        #'HOST': 'localhost',
        'HOST': 'methriks.mysql.pythonanywhere-services.com',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-gt'

TIME_ZONE = 'America/Guatemala'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
