from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from posts.models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'
    pagination_class = PageNumberPagination

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = IsAuthenticated, IsOwnerOrReadOnly
        else:
            self.permission_classes = IsAuthenticated,
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True)
    def like(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        post.like.add(request.user)
        post.unlike.remove(request.user)
        post.save()
        return Response({'response': 'you like this post'}, status=status.HTTP_200_OK)

    @action(detail=True)
    def unlike(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        post.unlike.add(request.user)
        post.like.remove(request.user)
        post.save()
        return Response({'response': 'you unlike this post'}, status=status.HTTP_200_OK)
