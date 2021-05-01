from rest_framework import serializers
from .models import *


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)


class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    title = serializers.CharField(max_length=100)
    text = serializers.CharField(max_length=100)


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Tokens.objects.create(**validated_data)
