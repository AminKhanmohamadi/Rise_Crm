
from .common import *

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'drf_spectacular',
]+ INSTALLED_APPS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Rise_db',
        'USER': 'postgres',
        'PASSWORD': 'aminkhm',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# Cors headers config
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5713",
]