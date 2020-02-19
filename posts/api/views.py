from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from posts.models import Post
from .serializers import PostSerializer


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def create_post(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes([IsAuthenticated, ])
def post_details(request, slug):

    post = get_object_or_404(Post, slug=slug)

    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if post.author != request.user:
        return Response({'response': ' only author can edit or delete post'})

    if request.method == "PUT":
        serializer = PostSerializer(post, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'successfully edited'
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        data = {}
        deleted = post.delete()
        if deleted:
            data['response'] = 'successfully deleted'
        else:
            data['response'] = 'failed to delete'
        return Response(data=data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'GET':
        post.like.add(request.user)
        post.unlike.remove(request.user)
        post.save()
        return Response({'response': 'you liked this post'}, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def unlike(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'GET':
        post.unlike.add(request.user)
        post.like.remove(request.user)
        post.save()
        return Response({'response': 'you liked this post'}, status=status.HTTP_200_OK)
