from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>[^\.]+)$', views.post, name='post'),
    url(r'^filter/$', views.filter, name='filter' ),
]