from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer
from users.utils import email_verify


@api_view(['POST', ])
@permission_classes([AllowAny])
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        email = request.data.get('email', '')
        if serializer.is_valid() and email_verify(email):
            serializer.save()
            data['response'] = 'User successfully registered'
            data['username'] = request.data['username']
            data['email'] = email
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
