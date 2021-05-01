from django.urls import path

from .views import *

app_name = 'api'

urlpatterns = [
    path('auth/', AuthView.as_view()),
    path('news/', NewsView.as_view())
]