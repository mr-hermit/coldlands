from django.db import models
from blog.models import UUIDField

class Menu(models.Model):
    menuid = UUIDField(primary_key=True, editable=False)
    site = models.ForeignKey("SiteNav", null=False) 
    name = models.CharField(max_length=50)
    parent = models.ForeignKey("Menu", null=True, blank=True)
    url = models.CharField(max_length=200, null=False, default="#")
    weight = models.IntegerField()
    auth = models.BooleanField(default = False)
    private = models.BooleanField(default = False)
        
    def __unicode__(self):
        return u"%s" % self.name
    
    def __str__(self):
        return self.__unicode__()
    
    
class SiteNav(models.Model):
    site = models.CharField(max_length=32)
    baseurl = models.URLField()
    
    def __unicode__(self):
        return u"%s" % self.site
    
    def __str__(self):
        return self.__unicode__()