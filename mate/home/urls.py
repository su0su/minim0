from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from home.views import api

app_name = 'home'


urlpatterns = [
    path('', api, name='home'),
]