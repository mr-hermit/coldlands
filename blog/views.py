from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post, Category


def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()[:5]
    })

def post(request, postid):
    return render_to_response('post.html', {
        'post': get_object_or_404(Post, postid=postid)
    })
    
# def filter(request, filter):
#     category = get_object_or_404(Category, catid=catid)
#     return render_to_response('view_category.html', {
#         'category': category,
#         'posts': Post.objects.filter(category=category)[:5]
#     })
    