'''
Created on Mar 2, 2016

@author: zolotko
'''

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter('get_object_url')
def get_object_url(value):
    return(value.get_absolute_url())

@register.filter('truncate_until')
@stringfilter
def truncate_until(value,arg):
    return(value.split(arg)[0])