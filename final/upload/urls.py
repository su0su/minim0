from django.urls import path

from . import views
from upload.views import upload,result

app_name='upload'

urlpatterns = [
    path('', upload ,name="upload"),
    path('result/', result ,name="result"),
      
]