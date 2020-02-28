import re
from chat.models import Messages
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = 'message', 'author', 'email', 'create_date', 'update_date', 'id'

