from django.core.asgi import get_asgi_application
from os import environ as env

env.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')
application = get_asgi_application()
