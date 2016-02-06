from django import template
from markdown import markdown
register = template.Library()
@register.filter(name='mark')
def mark(value):
    return markdown(value, extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite'])
