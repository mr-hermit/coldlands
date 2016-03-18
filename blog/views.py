from django.shortcuts import render, render_to_response
from django.core.exceptions import ObjectDoesNotExist
from blog.models import Post

def index(request):
    return render_to_response('blog/index.html', {
        'posts': Post.objects.all(),
    })

def post(request,post_id):
    try:
        post = Post.objects.get(post_id=post_id)
    except ObjectDoesNotExist:
        post = None
    return render_to_response('blog/post.html', {
        'post': post,
    })