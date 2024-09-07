from django import template
from django.urls import reverse, NoReverseMatch
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    # Получаем текущий URL страницы
    current_url = context['request'].path

    # Получаем все элементы меню с указанным именем
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent').order_by('order')

    # Функция для построения дерева меню
    def build_tree(parent=None):
        tree = []
        for item in menu_items:
            if item.parent == parent:
                tree.append({
                    'item': item,
                    'children': build_tree(item),
                    'is_active': is_active(item)
                })
        return tree

    # Функция для определения активного элемента
    def is_active(menu_item):
        if menu_item.url == current_url:
            return True
        try:
            # Проверяем по named URL
            if reverse(menu_item.named_url) == current_url:
                return True
        except NoReverseMatch:
            pass
        return False

    # Строим дерево меню
    menu_tree = build_tree()

    return {'menu_tree': menu_tree}

