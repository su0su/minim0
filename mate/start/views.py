from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import re


def validate_email(email):
    check_element = email.split("@")[0]
    return bool(re.search("[^a-zA-Z0-9]", check_element))

def validate_pw(pw):
    validate_codition = [
        lambda s: any(x.isupper() for x in s),
        lambda s: any(x.islower() for x in s),
        lambda s: any(x.isdigit() for x in s),
        lambda s: len(s) == len(s.replace(" ","")),
        lambda s: len(s) >= 10
    ]

    for validator in validate_codition:
        if not validator(pw):
            return True
# Create your views here.
def index(request):
    return render(request, 'hello.html')


def signup(request):#회원가입
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']

        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'], email = request.POST['email'])
        auth.login(request, user)
        return redirect('./')
    return render(request, 'signup.html')

def login(request):
    if request.user.is_authenticated:
        return redirect("/youtube")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None :
            auth.login(request, user)
            return redirect('/youtube')
        else :
            return render(request, 'login.html', {'error' : 'username or password is incorrect'})
    else :
        return render(request, 'login.html')


def logout(request):
    if request.method == "POSt":
        auth.logout(request)
        return redirect("./")
    return render(request, 'login.html')


