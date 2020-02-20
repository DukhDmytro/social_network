from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import Post
from .serializers import PostSerializer
from . import permissions


class BlogPost(APIView):
    """
    Create post instance or retrieve all instances.
    """
    permission_classes = [IsAuthenticated, permissions.IsOwnerOrReadOnly]

    def get(self, request):
        """
        Get all post instances
        """
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Retrieve post instance
        """
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    """
     Retrieve, update or delete a post instance.
    """
    permission_classes = [IsAuthenticated, permissions.IsOwnerOrReadOnly]

    def get_post(self, slug):
        post = get_object_or_404(Post, slug=slug)
        return post

    def get(self, request, slug):
        """
        Retrieve post instance by slug
        """
        post = self.get_post(slug=slug)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        """
        Update post instance by slug
        """
        post = self.get_post(slug=slug)
        if post.author != request.user:
            return Response({'response': ' only author can edit or delete post'})
        serializer = PostSerializer(post, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'successfully edited'
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        """
        Delete post instance by slug
        """
        post = self.get_post(slug=slug)
        if post.author != request.user:
            return Response({'response': ' only author can edit or delete post'})
        data = {}
        deleted = post.delete()
        if deleted:
            data['response'] = 'successfully deleted'
        else:
            data['response'] = 'failed to delete'
        return Response(data=data)


class Like(APIView):
    """
    Like post instance by slug
    """
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if request.method == 'GET':
            post.like.add(request.user)
            post.unlike.remove(request.user)
            post.save()
            return Response({'response': 'you like this post'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class Unlike(APIView):
    """
    Unlike post instance by slug
    """
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if request.method == 'GET':
            post.unlike.add(request.user)
            post.like.remove(request.user)
            post.save()
            return Response({'response': 'you unlike this post'}, status=status.HTTP_200_OK)
