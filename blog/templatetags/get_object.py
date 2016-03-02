'''
Created on Mar 1, 2016

@author: zolotko
'''

from django import template

register = template.Library()

@register.filter('get_object')
def get_object(value,arg):
    return(value)