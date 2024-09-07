from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class BaseModelAdmin(admin.ModelAdmin):
    """Base Model Admin"""
    list_per_page = 25


admin.site.site_header = _('DjangoShop Thee menu')
