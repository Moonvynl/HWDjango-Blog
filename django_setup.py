import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
django.setup()

from post_system.models import Author