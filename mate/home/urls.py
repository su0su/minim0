from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from home.views import youtubeapi

app_name = 'home'


urlpatterns = [
    path('', youtubeapi, name='home'),
]