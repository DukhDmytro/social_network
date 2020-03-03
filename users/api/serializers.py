from rest_framework import serializers
from django.contrib.auth.models import User
from users.utils import email_verify
from users.models import UserMessages


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        email_verify(validated_data['email'])
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessages
        fields = ['msg', ]
