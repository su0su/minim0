from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from main.views import index

app_name = 'main'


urlpatterns = [
    path('', index, name='main'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
]