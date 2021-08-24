from django.urls import path

from . import views
from main.views import main

app_name='main'

urlpatterns = [
    path('',main,name="main"),
    path('join/',views.join,name='join')
]