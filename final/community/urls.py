from django.urls import path

from . import views
from community.views import index, music_input, youtube_input, movie_input, playlist_input, sub_playlist_input

app_name='community'

urlpatterns = [
    path('', views.index, name="community"),
    path('db/', sub_playlist_input, name="db"),
]