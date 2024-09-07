from django.contrib import admin
from base.admin import BaseModelAdmin
from .forms import UserForm
from .models import User


@admin.register(User)
class UserAdmin(BaseModelAdmin):
    """User Admin panel"""
    form = UserForm
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'middle_name', ]
    list_display_links = list_display
    fields = ['id', 'email', 'first_name', 'last_name', 'password', 'groups', 'is_active',
              'is_superuser', 'is_staff', 'created', 'updated']
    readonly_fields = ['id', 'created', 'updated']
    list_filter = ['is_active', 'is_superuser', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name']
