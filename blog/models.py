from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30)
    creat_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s' % self.name
    def get_absolute_url(self):
        return reverse('blog.tag', args=[self.name])

class Category(models.Model):
    name = models.CharField(max_length=30)
    creat_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s' % self.name
    def get_absolute_url(self):
        return reverse('blog.category', args=[self.name])
    def get_post_count(self):
        return Post.objects.filter(category=self.id).count()

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=300)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag, blank=True)
    def __unicode__(self):
        return u'%s' % self.title
    
    def get_absolute_url(self):
        year = str(self.publish_time.year)
        month = str(self.publish_time.month)
        if len(month) == 1:
            month = '0' + month
        day = str(self.publish_time.day)
        return reverse('blog.post', args=[year,month,day,self.slug])
    def get_categories(self):
        return self.category.all()
    def get_tags(self):
        return self.tag.all()
