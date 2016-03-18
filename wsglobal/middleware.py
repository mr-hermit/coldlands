from wsglobal.models import HitCount
from django.db.models import F

class PageViewsMiddleware:
    def process_request(self, request, *args, **kwargs):
        if '/admin' not in request.path:
            hit, hit_created = HitCount.objects.get_or_create(url=request.path)
            hit.hits = F('hits') + 1
            hit.save()

        return None