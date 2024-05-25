"""
WSGI config for base project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from users.models import CustomUser
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')

application = get_wsgi_application()

users = CustomUser.objects.all()
if not users:
    CustomUser.objects.create_superuser(name="admin", email="admin@localhost.com", password="QVKL67KNtROt02s", is_superuser=True, is_staff=True)