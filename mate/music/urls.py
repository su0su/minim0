from django.urls import path

from . import views
from music.views import music

app_name='music'

urlpatterns = [
    path('',music,name="music")
    #url(r'^search/', views.search, name='search')
]