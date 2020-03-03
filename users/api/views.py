from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from .serializers import UserSerializer, UserMessageSerializer
from .permissions import IsOwnerOrReadOnly
from users.models import UserMessages


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = AllowAny,
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = IsAuthenticated, IsOwnerOrReadOnly
        else:
            self.permission_classes = IsAuthenticated,
        return super().get_permissions()

    @action(detail=True)
    def send_msg(self, request, pk):
        recipient = get_object_or_404(User, username=pk)
        sender = User.objects.get(pk=request.user.id)
        serializer = UserMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=sender, recipient=recipient)
        return Response({'response': request.data}, status=status.HTTP_201_CREATED)
