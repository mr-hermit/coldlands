from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post, Category

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()
    })