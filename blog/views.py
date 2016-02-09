from django.shortcuts import render, get_object_or_404
from .models import Post,Category,Tag,Page
from .utils import prev_next_post, paginator_process
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-publish_time')
    posts = paginator_process(posts, request)
    context = {'posts' : posts}
    return render(request, 'blog/archive.html', context)
def post(request, year, month, day, slug):
    post = get_object_or_404(Post, publish_time__year=int(year), publish_time__month=int(month), publish_time__day=int(day), slug=slug)
    return render(request, 'blog/post.html', {'post':post})
def category(request, name):
    cat = get_object_or_404(Category, name=name)
    posts = Post.objects.filter(category=cat.id).order_by('-publish_time')
    posts = paginator_process(posts, request)
    return render(request, 'blog/archive.html', {'posts':posts, 'category':name})
def tag(request, name):
    tag = get_object_or_404(Tag, name=name)
    posts = Post.objects.filter(tag=tag.id).order_by('-publish_time')
    posts = paginator_process(posts, request)
    return render(request, 'blog/archive.html', {'posts':posts, 'tag':name})
def archive(request, year, month):
    posts = Post.objects.filter(publish_time__year=int(year), publish_time__month=int(month)).order_by('-publish_time')
    posts = paginator_process(posts, request)
    return render(request, 'blog/archive.html', {'posts':posts, 'year': year, 'month':month})
def page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'blog/page.html', {'page':page})
def sitemap_view(request):
    categories = Category.objects.all()
    pages = Page.objects.all()
    return render(request, 'blog/sitemap.html', {'pages':pages, 'categories':categories}) 
