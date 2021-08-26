from django.urls import path

from . import views
from start.views import join, api, login

app_name='start'

urlpatterns = [
    path('', login ,name="login"),
    path('index/', api, name='index'),
    path('join/', join, name='join'),
    path('keyword/', views.keyword, name='keyword'),
    path('success/', views.success, name='success'),
    
]