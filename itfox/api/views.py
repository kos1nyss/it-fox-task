from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .forms import *

import time


class AuthView(APIView):
    def post(self, request):
        user = request.data.get('auth')
        user_s = UserSerializer(data=user)
        if user_s.is_valid(raise_exception=True):
            user_f = UserForm(user)
            if user_f.is_valid():
                token = Tokens(token=hash(time.time()))
                token.save()
                return Response({'token': token.token})
            return Response({'error': 'incorrect username or password'},
                            status=status.HTTP_400_BAD_REQUEST)


class NewsView(APIView):
    def get(self, request):
        token_s = TokenSerializer(data=request.GET)
        if token_s.is_valid(raise_exception=True):
            token = TokenForm(request.GET)
            if token.is_valid():
                news = News.objects.all()
                news_s = NewsSerializer(news, many=True)
                return Response({'news': news_s.data})
            return Response({'error': 'incorrect token'},
                            status=status.HTTP_400_BAD_REQUEST)
