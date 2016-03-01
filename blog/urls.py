from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<postid>[^\.]+)', views.post, name='post'),
#     url(r'^category/(?P<catid>[^\.]+)', views.view_category, name='view_category'),
]