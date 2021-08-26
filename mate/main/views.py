from django.shortcuts import render, redirect
from django.template import loader
from .models import Upload
from django.views.decorators.csrf import csrf_exempt
import urllib
import os
from django.http import HttpResponse, Http404
import mimetypes

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
    print(context)

    return render(request,'main/upload.html',{'profile':context})

