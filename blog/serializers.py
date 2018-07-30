from rest_framework import serializers
from taggit.models import Tag
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from .models import Post, Category, Link, Page


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    tag = TagListSerializerField()

    class Meta:
        model = Post
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = '__all__'