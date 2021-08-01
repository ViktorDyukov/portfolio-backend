"""
Django settings for vi2021 project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import environ

env = environ.Env()
environ.Env.read_env()





# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p#&maw721ync+d!451+a&7vxckw4)pz@tcz+h!6)m(w#$xgui9'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app2021',
    'rest_framework',
    'martor',
    'corsheaders',
    'adminsortable2',
    'validators',
    'easy_thumbnails',
    'environ',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}

ALLOWED_HOSTS = [
  'victorduco.com',
]

CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOWED_ORIGINS = (
    'https://victorduco.com',
)

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.victorduco\.com$",
]

ROOT_URLCONF = 'vi2021.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'vi2021.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djngdb',
        'USER': 'dj034',
        'PASSWORD': 'd45so!094jmPOgfvXFpf',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static_d/'
STATIC_ROOT = '/home/django/static'


# Other

DEFAULT_AUTO_FIELD='django.db.models.AutoField'
MEDIA_ROOT = '/home/django/media'
MEDIA_URL = '/media/'
FILE_UPLOAD_MAX_MEMORY_SIZE = int(10 * 1024 * 1024)

THUMBNAIL_ALIASES = {
    '': {
        'preview_desk_x1': {'size': (1334, 613), 'crop': True, 'quality': 85},
        'preview_desk_x2': {'size': (1334 * 2, 613 * 2), 'crop': True, 'quality': 85},
        'separatorImg_desk_x1': {'size': (1200, 750), 'crop': True, 'quality': 85},
        'separatorImg_desk_x2': {'size': (1200 * 2, 750 * 2), 'crop': True, 'quality': 85},
        'caseimg_x1': {'size': (1288, 800), 'crop': True, 'quality': 85},
        'caseimg_x2': {'size': (1288 * 2, 800 * 2), 'crop': True, 'quality': 85},
        'caseimg_preview_x1': {'size': (380, 236), 'crop': True, 'quality': 85},
        'caseimg_preview_x2': {'size': (380 * 2, 236 * 2), 'crop': True, 'quality': 85},

    },
}

PUB_CUSTOMIZATION = 2

try:
    dj_env = env('DJANGO_ENV')
except:
    dj_env = 'development'

if dj_env != 'production':
     from .local_settings import *