from django import template
from blog.models import Post,Category,Link
from taggit.models import Tag
from random import shuffle
register = template.Library()
@register.inclusion_tag('blog/sidebar/archive_list.html', takes_context = True)
def get_archive(context):
    return {'months': Post.objects.datetimes('publish_time', 'month')}
@register.inclusion_tag('blog/sidebar/category_list.html', takes_context = True)
def get_categories(context):
    return {'categories': Category.objects.all()}
@register.inclusion_tag('blog/sidebar/link_list.html', takes_context = True)
def get_links(context):
    return {'links': Link.objects.all()}
@register.inclusion_tag('blog/sidebar/tag_list.html', takes_context = True)
def get_tags(context):
    tags = Tag.objects.all()
    tags = list(tags) 
    shuffle(tags)
    tags = tags[:50]
    return {'tags': tags}
