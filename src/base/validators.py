import re

from django.conf import settings


def email_validate(email: str) -> bool | re.Match[str] | None:
    """Email validate"""
    if email:
        return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", f'{email}')
    return False


def validate_password(value: str) -> str | bool:
    """Validate password"""
    if value:
        if len(value) >= settings.PASSWORD_LENGTH:
            return value
    return False
