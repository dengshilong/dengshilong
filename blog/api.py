#coding: utf-8
from .models import Post, Category
from .serializers import PostSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics



class PostListAPI(generics.ListAPIView):
    """
    List all posts.
    """
    model = Post
    serializer_class = PostSerializer
    pagination_by = 10

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-publish_time')
        queryset = queryset.prefetch_related('category')
        return queryset

class PostAPI(generics.RetrieveUpdateAPIView):
    """
    List single post
    """
    model = Post
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        queryset = super(PostAPI, self).get_queryset()
        queryset = queryset.prefetch_related('category')
        return queryset


class CategoryAPI(generics.ListAPIView):
    """
    List all posts in category.
    """
    model = Post
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(category__in=self._category).order_by('-publish_time')
        queryset = queryset.prefetch_related('category')
        return queryset

    def get(self, request, *args, **kwargs):
        category = kwargs['category']
        category = Category.objects.filter(name=category)
        if not category.exists():
            return Response({"detail": u'不存在此分类'}, status=status.HTTP_404_NOT_FOUND)
        self._category = category
        return super(CategoryAPI, self).get(request, *args, **kwargs)

