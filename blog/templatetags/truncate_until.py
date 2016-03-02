'''
Created on Mar 1, 2016

@author: zolotko
'''

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter('truncate_until')
@stringfilter
def truncate_until(value):
    return(value.split('<p>')[0])
