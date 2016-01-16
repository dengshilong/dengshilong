from django.shortcuts import render, get_object_or_404
from .models import Post
from .utils import get_page,prev_next_post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-publish_time')
    page = get_page(request)
    paginator = Paginator(post_list, 10) 
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts' : posts}
    return render(request, 'blog/index.html', context)
def post(request, year, month, day, slug):
    post = get_object_or_404(Post, publish_time__year=int(year), publish_time__month=int(month), publish_time__day=int(day), slug=slug)
    return render(request, 'blog/post.html', {'post':post})
