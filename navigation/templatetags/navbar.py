'''
Created on Mar 3, 2016

@author: zolotko
'''

from django import template
from navigation.models import Menu

register = template.Library()

# class MenuObject(template.Node):
#     def __init__(self):
#         pass
#     
#     def render(self, context):
# #         template.Node.render(self, context)
# #         current_path = context['request'].path
# #         user = context['request'].user
#         context['menus'] = Menu.objects.all()
#         return ''        
#         

@register.inclusion_tag('navbar.html', takes_context=True)
def navbar(context):
    return {
        'menus': Menu.objects.all(),
        }