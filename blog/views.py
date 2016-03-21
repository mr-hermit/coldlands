from django.shortcuts import render, render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from blog.models import Post,Tag

def index(request):
    return render_to_response('blog/index.html', {
        'posts': Post.objects.all(),
        'tags': Tag.objects.all(),
        'dates': Post.objects.dates('posted','month').distinct()
    })

def post(request,post_id):
    try:
        post = Post.objects.get(post_id=post_id)
        tags = post.tags.all()
    except ObjectDoesNotExist:
        post = None
    return render_to_response('blog/post.html', {
        'post': post,
        'tags': tags,
    })

# TODO: Change the filter view to accep and parse multiple parameters and values
def filter(request):
    tags=request.GET.get('tags','')
    qfilter = Q(tags=tags)

    try:
        posts = Post.objects.complex_filter(qfilter)
    except Post.DoesNotExist:
        posts = None

    siteinfo={
        'title': 'Filtered blog records',
        'ctag': tags,
    }

    return render_to_response('blog/index.html', {
        'siteinfo': siteinfo,
        'posts': posts,
        'tags': Tag.objects.all(),
        'ctag': Tag.objects.get(Q(tag=tags))
    })
