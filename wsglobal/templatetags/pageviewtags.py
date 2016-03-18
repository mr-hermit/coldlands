from django import template
from wsglobal.models import HitCount

register = template.Library()

@register.simple_tag(takes_context=True)
def pageviews(context):
    try:
        request = context['request']
        hit = HitCount.objects.get(url=request.path)
        return hit.hits
    except HitCount.DoesNotExist:
        return 0