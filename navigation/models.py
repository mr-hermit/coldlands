from __future__ import unicode_literals
from wsglobal.models import Site

from django.db import models

class NavItem(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    visible = models.BooleanField()

    def __unicode__(self):
        return u"%s" % self.site.name

    def __str__(self):
        return self.__unicode__()

class NavItemNested(models.Model):
    parent = models.ForeignKey(NavItem, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200,default="#")

    def __unicode__(self):
        return u"%s" % self.title

    def __str__(self):
        return self.__unicode__()
