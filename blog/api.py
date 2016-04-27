from .models import Post
from .serializers import PostSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


class PostListAPI(generics.ListAPIView):
    """
    List all posts.
    """
    model = Post
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-publish_time')
        return queryset

class PostDetailAPI(APIView):
    """
    List single post
    """
    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(pk=kwargs['pk'])
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

class CategoryAPI(generics.ListAPIView):
    """
    List all posts in category.
    """
    model = Post
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(category=self._category).order_by('-publish_time')
        return queryset

    def get(self, request, *args, **kwargs):
        self._category = kwargs['category']
        return super(CategoryAPI, self).get(request, *args, **kwargs)

