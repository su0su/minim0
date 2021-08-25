from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from comm.views import sign_up_keyword,test_content_insert_music

app_name = 'comm'


urlpatterns = [
    path('insert/', test_content_insert_music, name='music'),
    path('', test_content_insert_music, name='keyword'),
]