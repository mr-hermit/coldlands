from django import template
from django.db.models import Q

from navigation.models import NavItem,NavItemNested

register = template.Library()

@register.inclusion_tag('navbar.html', takes_context=True)
def navbar(context):
    return {
        'navitems': NavItem.objects.all(),
    }

@register.simple_tag
def navnitem(*args, **kwargs):
    parent_item = kwargs['navitem']
    return NavItemNested.objects.filter(parent=parent_item)