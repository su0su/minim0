from django.urls import path

from . import views
from movie.views import index

urlpatterns = [
    path('', index, name='movie'),
]