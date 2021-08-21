from django.urls import path

from . import views
from youtube.views import youtube

urlpatterns = [
    path('', youtube, name='youtube'),
]