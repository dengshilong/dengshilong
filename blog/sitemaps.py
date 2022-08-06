
from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from .models import Post
class BlogSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'
    protocol = 'http'

    def items(self):
        return Post.objects.all().order_by("-publish_time")

    def location(self, item):
        return item.get_absolute_url()
