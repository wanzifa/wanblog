from __future__ import unicode_literals
from django.db import models
from markdown import markdown
from django.template.defaultfilters import slugify
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.localtime(timezone.now()))
    #slug = models.SlugField(default=' ')
    tag = models.ForeignKey(Tag)

    def save(self, *args, **kwargs):
        #self.slug = slugify(self.title)
        self.body = markdown(self.body)
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title



