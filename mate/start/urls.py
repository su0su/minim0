from django.urls import path
from . import views
from start.views import index, login, signup

urlpatterns = [
    path('', index, name='start'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    
]