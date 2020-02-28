from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from chat.models import Messages
from .serializers import MessageSerializer


class MessagesViewSet(ModelViewSet):
    permission_classes = AllowAny,
    serializer_class = MessageSerializer
    queryset = Messages.objects.all()
    pagination_class = PageNumberPagination
    http_method_names = 'get', 'post'
    lookup_field = 'id'
