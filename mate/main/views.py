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