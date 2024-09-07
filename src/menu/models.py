from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel, NULLABLE
from users.models import CreatedByMixin


class MenuItem(BaseModel, CreatedByMixin):
    title = models.CharField(_('title'), max_length=200)
    url = models.CharField(_('url'), max_length=200, **NULLABLE)
    named_url = models.CharField(_('named_url'), max_length=200, **NULLABLE)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, **NULLABLE, related_name='children'
    )
    menu_name = models.CharField(_('menu_name'), max_length=50)
    order = models.PositiveIntegerField(_('order'), default=0)

    class Meta:
        verbose_name = _('Пункт меню')
        verbose_name_plural = _('Пункты меню')
        db_table = _('menu_item')
        ordering = ['order']

    def __str__(self):
        return self.title
