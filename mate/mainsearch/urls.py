from django.urls import path

from . import views
from mainsearch.views import search

app_name='mainsearch'

urlpatterns = [
    path('',search,name="mainsearch")
    #url(r'^search/', views.search, name='search')
]