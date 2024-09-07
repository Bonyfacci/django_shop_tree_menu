from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel, LowerCaseEmailField, NULLABLE


class User(AbstractUser, BaseModel):
    """User model"""
    username = models.CharField(_('Username'), max_length=150, unique=True, help_text=_("Уникальное имя пользователя"))

    first_name = models.CharField(_('first_name'), max_length=150, help_text=_("Имя пользователя"))
    last_name = models.CharField(_('last_name'), max_length=150, help_text=_("Фамилия пользователя"))
    middle_name = models.CharField(_('middle_name'), max_length=150, **NULLABLE, help_text=_("Отчество пользователя"))

    email = LowerCaseEmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')


class CreatedByMixin(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                   related_name="%(class)s_created",
                                   verbose_name=_('Пользователь'))

    class Meta:
        abstract = True
