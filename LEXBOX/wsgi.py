"""
WSGI config for LEXBOX project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise

application = get_wsgi_application()

application = WhiteNoise(application)
application.add_files('/LEXBOXapp/static/files', prefix='more-files/')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LEXBOX.settings')



