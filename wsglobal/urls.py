from django.conf.urls import url

from wsglobal import views

urlpatterns = [
    url(r'^$', views.cover, name='cover'),
    url(r'^contacts', views.contacts, name='contacts'),
]