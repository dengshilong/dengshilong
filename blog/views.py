from django.shortcuts import render, get_object_or_404
from .models import Post,Category,Page
from .utils import prev_next_post, paginator_process
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
# Create your views here.
class PostList(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.all().order_by('-publish_time')

class PostDetail(DetailView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(publish_time__year=self.kwargs['year'], publish_time__month=self.kwargs['month'], 
            publish_time__day=self.kwargs['day'], slug=self.kwargs['slug'])
        
class CategoryList(ListView):
    model = Post
    def get_queryset(self):
        cat = get_object_or_404(Category, name=self.kwargs['category'])
        return Post.objects.filter(category=cat.id).order_by('-publish_time')

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['category'] = self.kwargs['category']
        return context
     

class TagList(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(tag__name=self.kwargs['tag']).order_by('-publish_time')
    def get_context_data(self, **kwargs):
        context = super(TagList, self).get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag']
        return context

class ArchiveList(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(publish_time__year=self.kwargs['year'], publish_time__month=self.kwargs['month']).order_by('-publish_time')
    def get_context_data(self, **kwargs):
        context = super(ArchiveList, self).get_context_data(**kwargs)
        context['year'] = self.kwargs['year']
        context['month'] = self.kwargs['month']
        return context

class PageDetail(DetailView):
    model = Page
    def get_queryset(self):
        return Page.objects.filter(slug=self.kwargs['slug'])  

class SitemapList(ListView):
    template_name = 'blog/sitemap.html'
    model = Category
    context_object_name = 'categories'
    def get_context_data(self, **kwargs):
        context = super(SitemapList, self).get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        return context
