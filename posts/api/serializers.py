from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField('get_author')

    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'date_created', 'date_edited', 'author']

    def get_author(self, post):
        return post.author.username

