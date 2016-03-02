'''
Created on Mar 1, 2016

@author: zolotko
'''

from django import template

register = template.Library()

@register.filter('get_object_url')
def get_object_url(value):
    return(value.get_absolute_url())
