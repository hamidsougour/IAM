"""
Django settings for iam project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import django
from django.utils.encoding import force_str
django.utils.encoding.force_text=force_str

from pathlib import Path
from . info import *

EMAIL_USE_TLS= EMAIL_USE_TLS
EMAIL_HOST= EMAIL_HOST
EMAIL_HOST_USER= EMAIL_HOST_USER
EMAIL_HOST_PASSWORD= EMAIL_HOST_PASSWORD
EMAIL_PORT=EMAIL_PORT

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k8!4#_4=kq-idc1n7$%hwqmf&0811wvq+u-ngf4p%1)zh0ttkc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'adminlte3_theme',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap_modal_forms',
    'widget_tweaks',
    'authentication',
    'utilisateur',
    'django_cleanup.apps.CleanupConfig',
]
#'two_factor',

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'iam.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'iam.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'authentication.validators.ContainsLetterValidator',
    },
]





# Paramètres de nettoyage pour supprimer les fichiers associés aux utilisateurs supprimés
# Assurez-vous d'avoir défini le champ approprié dans votre modèle d'utilisateur personnalisé pour stocker le fichier
CLEANUP_KEEP_AUTHENTICATED = False
CLEANUP_REPLACE_WITH_FIELD = 'avatar'  # Remplacez 'avatar' par le nom du champ qui stocke le fichier dans votre modèle utilisateur personnalisé

# Durée (en jours) avant de supprimer un compte fantôme (compte inactif)
# Modifier cette valeur selon vos besoins
ACCOUNT_DELETE_DELAY = 30  # Exemple : supprimer le compte si l'utilisateur est inactif depuis 30 jours

# Configuration des tâches planifiées avec django-cleanup
CLEANUP_DELETE_ONLY = False
CLEANUP_DELETE_CHUNK_SIZE = 1000
CLEANUP_KEEP_PARENT = False
CLEANUP_USE_CONCURRENT = True
CLEANUP_SCHEDULE_PERIOD = 24 * 60 * 60  # Une fois par jour (en secondes)


import os

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = 'static/'
import os
STATIC_ROOT=os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media/')

JAZZMIN_SETTINGS = {
     # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "IAM",
    # Welcome text on the login screen
    "welcome_sign": "Systeme de gestion des accès et des identités (IAM)",
}


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
CRISPY_TEMPLATE_PACK = 'bootstrap5'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL='/static/'
AUTH_USER_MODEL = 'authentication.CustomUser'
LOGIN_URL='loginPage'
LOGIN_REDIRECT_URL='index'
LOGOUT_REDIRECT_URL=LOGIN_URL
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'