#coding:utf-8
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from .models import Post
from markdown import markdown

class LatestEntriesFeed(Feed):
    title = "邓世龙的自留地"
    link = "/feed/"
    description = "兼济天下则达，独善其身则穷"

    def items(self):
        return Post.objects.order_by('-publish_time')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return markdown(item.content)

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        #return reverse('blog.post', args=[item.pk])
        return item.get_absolute_url()
    def item_pubdate(self, item):
        return item.publish_time
