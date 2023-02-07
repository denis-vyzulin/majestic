from .base import *


# Important settings
DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = 'django-insecure-w)is-4wd048#^*y+)8kha+g=i%k3$@aqf4jitt@a)j)wq4b$6%'

# Application definition
WSGI_APPLICATION = 'config.wsgi.application'


# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'majestic/assets/',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')


# Sitemap file
INSTALLED_APPS += ['django.contrib.sitemaps']
