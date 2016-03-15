from __future__ import unicode_literals

from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    url = models.CharField(max_length=200)

    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return self.__unicode__()