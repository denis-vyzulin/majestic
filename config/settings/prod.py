from .base import *
from os import environ as env


# Important variables
DEBUG = False
SECRET_KEY = env.get('DJANGO_SECRET_KEY', 'django-insecure-)*gf_-pcx3=s!-1#l9^zjek2kl+(dn_ua1oh4@_m%q*y%o2+2m')
ALLOWED_HOSTS = env.get('DJANGO_ALLOWED_HOSTS', '127.0.0.1 localhost').split(" ")


# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.get('DB_NAME', 'db_name'),
        'USER': env.get('DB_USER', 'db_user'),
        'PASSWORD': env.get('DB_PASSWORD', 'db_password'),
        'HOST': env.get('DB_HOST', 'localhost'),
        'PORT': '3306',
    }
}


# Application definition
WSGI_APPLICATION = 'config.server.application'


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'majestic/assets/',
]
STATIC_ROOT = BASE_DIR.parent.joinpath('static')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')


# Sitemap file
INSTALLED_APPS += ['django.contrib.sitemaps']
