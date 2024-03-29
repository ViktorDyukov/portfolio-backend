import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tnm2021',
        'USER': 'tnm_user',
        'PASSWORD': 'Keepe2021',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'api/media/'

ALLOWED_HOSTS = [
  'localvictor.com',
]

CORS_ALLOWED_ORIGINS = (
    'http://localvictor.com:3000',
)

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http://\w+\.localvictor\.com\:3000$",
]

PUB_CUSTOMIZATION = 4

LOGGING = {}