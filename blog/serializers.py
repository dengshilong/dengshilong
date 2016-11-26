from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    tag = TagListSerializerField()

    class Meta:
        model = Post
