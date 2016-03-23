"""
WSGI config for coldlands project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import socket

from django.core.wsgi import get_wsgi_application


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coldlands.settings")
if socket.gethostname() == 'ws-2227':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coldlands.settings")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coldlands.settings_prod")

application = get_wsgi_application()
