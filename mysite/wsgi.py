"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

from pathlib import Path

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")


# BASE_DIR = parent of manage.py file
BASE_DIR = Path(__file__).resolve().parent 

# NOTE: This line will let Django handle models in the root folder
sys.path.append(str(BASE_DIR.parent))


application = get_wsgi_application()
