from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Site(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    url = models.CharField(max_length=200)

    def __unicode__(self):
        return u"%s" % self.name

class SiteInfo(models.Model):
    site = models.OneToOneField('Site', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    desc = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.title

class HitCount(models.Model):
    created = models.DateField(_('Created'),auto_now_add=True,editable=False)
    modified = models.DateField(_('Modified'),auto_now=True,editable=False)
    url = models.CharField(_('URL'),max_length=200)
    hits = models.PositiveIntegerField(_('Hits'),default=0)

    class Meta:
        ordering = ('-created','-modified')
        get_latest_by = 'created'

class Message(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    content = models.TextField()
