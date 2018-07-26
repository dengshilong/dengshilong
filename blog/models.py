from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    creat_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % self.name
    def get_absolute_url(self):
        return reverse('blog.category', args=[self.name])
    def get_post_count(self):
        return Post.objects.filter(category=self.id).count()
    def get_post(self):
        return Post.objects.filter(category=self.id)


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, allow_unicode=True, unique=True)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    tag = TaggableManager(blank=True)

    def __unicode__(self):
        return u'%s' % self.title
    
    def get_absolute_url(self):
        year = str(self.publish_time.year)
        month = str(self.publish_time.month)
        if len(month) == 1:
            month = '0' + month
        day = str(self.publish_time.day)
        if len(day) == 1:
            day = '0' + day
        return reverse('blog.post', args=[year,month,day,self.slug])

    def get_categories(self):
        return self.category.all()

    def get_tags(self):
        return self.tag.all()


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, allow_unicode=True, unique=True)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s' % self.title
    def get_absolute_url(self):
        return reverse('blog.page', args=[self.slug])


class Link(models.Model):
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    def __unicode__(self):
        return u'%s' % self.name
