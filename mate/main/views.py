from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def main(request):  

    return render(request,'main/login.html')

def join(request):  
    
    return render(request,'main/join.html')

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