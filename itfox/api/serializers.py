from rest_framework import serializers
from .models import *

from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    title = serializers.CharField(max_length=100)
    text = serializers.CharField(max_length=1000)


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def validate(self, data):
        username = data.get('username')
        users = User.objects.filter(username=username)
        if not users:
            raise serializers.ValidationError('Incorrect username')
        user = users[0]
        if not check_password(data['password'], user.password):
            raise serializers.ValidationError('Incorrect password')
        return data


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=100)

    def validate_token(self, token):
        if not Tokens.objects.all().filter(token=token):
            raise serializers.ValidationError('Incorrect token')
        return token
