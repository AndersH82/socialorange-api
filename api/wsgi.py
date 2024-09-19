import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the codex_api directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'api'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

application = get_wsgi_application()
