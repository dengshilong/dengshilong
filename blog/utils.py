from rest_framework.pagination import PageNumberPagination

from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_page(request):
    page = request.GET.get('page', '') 
    if not page:
        page = 1 
    return page
def prev_next_post(id):
    id = int(id)
    prev_id = id - 1 
    next_id = id + 1 
    try:
        prev_post = Post.objects.get(pk=prev_id)
    except:
        prev_post = None
    try:
        next_post = Post.objects.get(pk=next_id)
    except:
        next_post = None
    return prev_post,next_post
def paginator_process(posts, request):
    page = get_page(request)
    paginator = Paginator(posts, 10)  
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return posts


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100