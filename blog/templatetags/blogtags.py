from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter('preview')
@stringfilter
def preview(value):
    return value.split('%endpreview%')[0]