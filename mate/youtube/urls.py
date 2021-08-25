from django.urls import path

from . import views
from youtube.views import youtube, music, movie

urlpatterns = [
    path('', youtube, name='youtube'),
]