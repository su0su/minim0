from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from main.views import index, signup, login, logout

app_name = 'main'


urlpatterns = [
    path('', index, name='main'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', auth_views.LoginView.as_view(template_name='login.html'), name='logout'),
]