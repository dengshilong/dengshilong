from django import template
from markdown import markdown
from blog.models import Page
register = template.Library()
@register.inclusion_tag('blog/page_list.html', takes_context = True)
def get_pages(context):
    return {'pages': Page.objects.all()}
