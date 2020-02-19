from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField('get_author')
    like_count = serializers.SerializerMethodField('get_likes')

    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'date_created', 'date_edited', 'author', 'like_count']

    def get_author(self, post):
        return post.author.username

    def get_likes(self, post):
        return post.like.count() - post.unlike.count()
