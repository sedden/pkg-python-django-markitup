from django.db import models

from markitup.fields import MarkupField

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = MarkupField('body of post')

    def __unicode__(self):
        return self.title

class NoRendered(models.Model):
    """
    Test that the no_rendered_field keyword arg works. This arg should
    never be used except by the South model-freezing.

    """
    body = MarkupField(no_rendered_field=True)
