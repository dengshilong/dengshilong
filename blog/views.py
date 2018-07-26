# coding: utf-8
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from taggit.models import Tag

from blog.serializers import LinkSerializer, PostSerializer, CategorySerializer, TagSerializer, PageSerializer
from blog.utils import StandardResultsSetPagination
from .models import Post,Category,Page, Link
from django.views.generic import ListView, DetailView

# Create your views here.
class PostList(ListView):
    model = Post
    def get_queryset(self):
        queryset = Post.objects.all().order_by('-publish_time')
        queryset = queryset.prefetch_related('category')
        queryset = queryset.prefetch_related('tag')
        return queryset


class PostDetail(DetailView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(publish_time__year=self.kwargs['year'], publish_time__month=self.kwargs['month'], 
            publish_time__day=self.kwargs['day'], slug=self.kwargs['slug'])


class CategoryList(ListView):
    model = Post
    def get_queryset(self):
        cat = get_object_or_404(Category, name=self.kwargs['category'])
        queryset = Post.objects.filter(category=cat.id).order_by('-publish_time')
        queryset = queryset.prefetch_related('tag', 'category')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['category'] = self.kwargs['category']
        return context
     

class TagList(ListView):
    model = Post
    def get_queryset(self):
        queryset = Post.objects.filter(tag__name=self.kwargs['tag']).order_by('-publish_time')
        queryset = queryset.prefetch_related('tag', 'category')
        return queryset
    def get_context_data(self, **kwargs):
        context = super(TagList, self).get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag']
        return context


class ArchiveList(ListView):
    model = Post
    def get_queryset(self):
        queryset = Post.objects.filter(publish_time__year=self.kwargs['year'], publish_time__month=self.kwargs['month']).order_by('-publish_time')
        queryset = queryset.prefetch_related('tag', 'category')
        return queryset

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


class LinkViewSet(ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    pagination_class = None


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        params = self.request.query_params
        queryset = super(PostViewSet, self).get_queryset()
        category = params.get('category', None)
        if category:
            queryset = queryset.filter(category__name=category)
        tag = params.get('tag', None)
        if tag:
            queryset = queryset.filter(tag__name=tag)
        year = params.get('year', None)
        month = params.get('month', None)
        day = params.get('day', None)
        slug = params.get('slug', None)
        if year:
            queryset = queryset.filter(publish_time__year=year)
        if month:
            queryset = queryset.filter(publish_time__month=month)
        if day:
            queryset = queryset.filter(publish_time__day=day)
        if slug:
            queryset = queryset.filter(slug=slug)
        queryset = queryset.prefetch_related('tag', 'category')
        queryset = queryset.order_by('-publish_time')
        return queryset


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


class MonthsAPI(APIView):

    def get(self, request, *args, **kwargs):
        months = list(Post.objects.datetimes('publish_time', 'month').all())
        months.reverse()
        return Response(months, status=status.HTTP_200_OK)


class PageViewSet(ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    pagination_class = None

    def get_queryset(self):
        queryset = super(PageViewSet, self).get_queryset()
        params = self.request.query_params
        slug = params.get('slug', None)
        if slug:
            queryset = queryset.filter(slug=slug)
        return queryset