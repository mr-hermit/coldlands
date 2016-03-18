from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink

from uuid import uuid4
from datetime import date,timedelta

from wsglobal.models import Site


class UUIDField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length',16)
        kwargs['blank'] = True
        models.CharField.__init__(self, *args, **kwargs)

    def pre_save(self, model_instance, add):
        if add:
            value = str(uuid4().hex)[:16]
            setattr(model_instance,self.attname,value)
            return value
        else:
            return super(models.CharField, self).pre_save(model_instance,add)


class Post(models.Model):
    post_id = UUIDField(primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    text = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    auth = models.BooleanField()

    def __unicode__(self):
        return u"%s" % self.title

    @permalink
    def get_absolute_url(self):
        return ('post', None, {'post_id': str(self.post_id)} )

    def is_pass_due(self):
        if self.posted > date.today() - timedelta(7):
            return True
        return False

    class Meta:
        ordering=['posted']
