"""
ASGI config for moto_style project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
# Imports
# 3rd party:
import os

from django.core.asgi import get_asgi_application
# -----------------------------------------------------------------------------

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moto_style.settings')

application = get_asgi_application()
