from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly


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

