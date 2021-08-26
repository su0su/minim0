from django.shortcuts import render
from django.template import loader
from .models import Upload
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import urllib.request

# Create your views here.
def main(request):  

    return render(request,'main/login.html')

def join(request):  
    
    return render(request,'main/join.html')
    
@csrf_exempt
def keyword(request):
    if request.method == 'POST':
        selected = request.POST.getlist('keyword[]')
        print(selected)

    return render(request,'main/keyword.html')

def success(request):
    if request.method == 'POST':
        login = request.POST.getlist('login[]')
        print(login)
    return render(request, 'main/success.html')

def joinsuccess(request):
    if request.method == 'POST':
        join = request.POST.getlist('join[]')
        print(join)
    return render(request, 'main/joinsuccess.html')

def upload(request):
    return render(request, 'main/upload.html')

def upload_create(request):
    form=Upload()
    form.title=request.POST['title']
    form.keyword = request.POST.getlist('keyword[]')
    form.media=request.POST['media']
    form.url=request.POST['url']
    try:
        form.image=request.FILES['image']
    except: 
        pass
    form.save()
    
    context = {
        'title':form.title,
        'keyword':form.keyword,
        'image':form.image,
        'media':form.media,
        'url':form.url
    }

    return render(request,'main/upload.html',{'profile':context})

def download(request):
    # form=Upload()
    # url=form.image.url
    testurl="http://news.samsungdisplay.com/wp-content/uploads/2018/08/8.jpg"

    #download
    urllib.request.urlretrieve(testurl,"test22.jpg")
    return render(request,'main/upload.html',)
    
