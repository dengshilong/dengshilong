from rest_framework import serializers
from taggit.models import Tag
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from .models import Post, Category, Link


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    tag = TagListSerializerField()

    class Meta:
        model = Post

class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag