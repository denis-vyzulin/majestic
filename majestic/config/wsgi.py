from django.core.wsgi import get_wsgi_application
from os import environ as env


env.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
application = get_wsgi_application()
