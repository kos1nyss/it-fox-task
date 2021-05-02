from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *

import time


class AuthView(APIView):
    def post(self, request):
        user = request.data.get('auth')
        user_s = UserSerializer(data=user)
        if user_s.is_valid(raise_exception=True):
            token = Tokens(token=hash(time.time()))
            token.save()
            return Response({'token': token.token})

class NewsView(APIView):
    def get(self, request):
        token = TokenSerializer(data=request.GET)
        if token.is_valid(raise_exception=True):
            news = News.objects.all()
            news_s = NewsSerializer(news, many=True)
            return Response({'news': news_s.data})
