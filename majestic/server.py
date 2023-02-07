import sys
from os import environ as env


try:
    sys.path.remove('/usr/lib/python3/dist-packages')
except:
    pass

sys.path.append(env.get('DJANGO_PROJECT_PATH'))
sys.path.append(env.get('PYTHON_PACKAGES_PATH'))

env.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
