from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand

from users.models import User
from django.conf import settings


class Command(BaseCommand):
    """Command to create a superuser"""

    def handle(self, *args, **options):
        if settings.ADMIN_EMAIL and settings.ADMIN_PASSWORD:
            password = make_password(settings.ADMIN_PASSWORD)
            data = {
                'first_name': 'admin',
                'last_name': 'admin',
                'is_active': True,
                'is_staff': True,
                'is_superuser': True,
                'password': password,
            }
            User.objects.update_or_create(
                username=settings.ADMIN_USERNAME,
                email=settings.ADMIN_EMAIL,
                defaults=data
            )
