from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel, NULLABLE
from users.models import CreatedByMixin


class Category(BaseModel, CreatedByMixin):
    name = models.CharField(_('name'), max_length=200, unique=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, **NULLABLE, related_name='children'
    )
    slug = models.SlugField(_('slug'), max_length=200, unique=True)

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
        db_table = _('category')
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(BaseModel, CreatedByMixin):
    name = models.CharField(_('name'), max_length=200)
    description = models.TextField(_('description'), )
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    slug = models.SlugField(_('slug'), max_length=200, unique=True)

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')
        db_table = _('product')
        ordering = ['name']

    def __str__(self):
        return self.name
