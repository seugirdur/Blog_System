#transformando para JSON para uso da API

from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'thumbnail', 'excepts', 'content', 'slug', 'published', 'author', 'status')