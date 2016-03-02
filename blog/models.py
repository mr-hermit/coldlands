from django.db import models
from django.db.models import permalink
from uuid import uuid4

class UUIDField(models.CharField):
    
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 32 )
        kwargs['blank'] = True
        models.CharField.__init__(self, *args, **kwargs)
    
    def pre_save(self, model_instance, add):
        if add :
            value = str(uuid4().hex)
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(models.CharField, self).pre_save(model_instance, add)
    

class Post(models.Model):
    postid = UUIDField(primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    text = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('Category')
#    tag = models.ManyToManyField('Tag', null=True)
    
    def __unicode__(self):
        return '%s' % self.title
    
    @permalink
    def get_absolute_url(self):
        return ('post', None, {'postid': str(self.postid)})
    
    class Meta:
        ordering = ['posted']

class Category(models.Model):
    catid = UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, db_index=True)
    
    def __unicode__(self):
        return '%s' % self.name
    
    @permalink
    def get_absolute_url(self):
        return ('category', None, {'catid': self.catid})
    
class Tag(models.Model):
    tagid = UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=32, db_index=True)
    
    def __unicode_(self):
        return '%s' % self.name
    
    @permalink
    def get_absolute_url(self):
        return('filter', None, {'tagid': self.tagid})
    