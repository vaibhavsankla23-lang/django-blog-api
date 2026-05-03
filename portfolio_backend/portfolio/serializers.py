from rest_framework import serializers
from .models import Post, Project

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content',
                  'author', 'created_at', 'is_published']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'tech_stack',
                  'github_link', 'live_link', 'created_at']