from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.forms import UsernameField  
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from django.views import View
import bcrypt
import jwt
import re
from .models import TestMember
from my_settings import SECRET


def index(request):
    return render(request, 'hello.html')
    #return HttpResponse("Hello, world. You're at the polls index.")


#회원가입
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

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    res_data = {} #프론트에 던져줄 응답 데이터
    if request.method == "POST":
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        nickname = request.POST['nickname']

        User = get_user_model()
        #User.objects.all()
        # 비밀번호가 다르면 리턴
        if password1 != password2:
            res_data['error']="비밀번호가 다릅니다"
        elif validate_email(email) :
            res_data['error']="이메일 형식이 다릅니다."
        #elif validate_pw(password1):
            #res_data['error']="대소문자 그리고 숫자를 포함하여 10자리 이상이어야 합니다."
        elif User.objects.filter(username=nickname).exists():
            res_data['error']="이미 존재하는 아이디입니다."
        elif User.objects.filter(email=email).exists():
            res_data['error']="이미 존재하는 이메일입니다."
        else :
            hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
            #인스턴스 생성
            #user = TestMember.objects.create_user(email = email, password = hashed_password, nickname = nickname)
            user = TestMember.objects.create(email = email, password = hashed_password.decode('utf-8'), nickname = nickname )
            user.save()

    return render(request, 'signup.html', res_data)


def login(request):

    res_data = {}
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        password = request.POST['password']
        email = request.POST['email']
        name = request.POST['nickname']
        if not (email and password):
            res_data['error'] = "모든 칸을 다 입력해주세요"
        elif TestMember.objects.filter(email=email).exists():
            user = TestMember.objects.get(email=email, nickname=name)
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')) :
                access_token = jwt.encode({'email' : email}, SECRET, algorithm = "HS256")
                res = JsonResponse({"success":True})
                res.set_cookie('access_token', access_token.decode('utf-8') )

                #request.session['user'] = TestMember.nickname 
                #user_nickname = request.session.get('user') 
                #print("user_nick", user_nickname) 
                #info = TestMember.objects.get(pk=user_nickname) 
                #res_data['error'] = info               # 유니코드 문자열로 디코딩
                return redirect('/')
            else :
                res_data['error'] = "오류"

        
    return render(request, 'login.html', res_data)

def logout(request):
    reset = ''
    res = JsonResponse({'success':True})
    res.set_cookie('access_token', reset)
    return res

def check(request):
    res_data = {}
    user_nickname = request.session.get('user')
    if user_nickname :
        info = TestMember.objects.get(pk=user_nickname)
        res_data['error'] = info

        return render(request, 'login.html', res_data)




    