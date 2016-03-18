from django.shortcuts import render_to_response, get_object_or_404
from models import Site,SiteInfo

from django.core.exceptions import ObjectDoesNotExist

def index(request):
    try:
        siteinfo = SiteInfo.objects.get(site=Site.objects.get(name='ColdLands'))
    except ObjectDoesNotExist:
        siteinfo = None

    return render_to_response('index.html', {
        'siteinfo': siteinfo,
    })