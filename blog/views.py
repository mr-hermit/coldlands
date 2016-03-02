from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post, Category


def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()
    })

def post(request, postid):
    return render_to_response('post.html', {
        'post': get_object_or_404(Post, postid=postid)
    })
    
def category(request, catid):
    category = get_object_or_404(Category, catid=catid)
    return render_to_response('filter.html', {
        'category': category,
        'posts': Post.objects.filter(category=catid)
    })
    