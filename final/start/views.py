from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth, messages
import re
from django.db import connection
import my_settings
import requests
from isodate import parse_duration
import json
import urllib.request

def validate_email(email): # 이메일 유효성 검사
    check_element = email.split("@")[0]
    return bool(re.search("[^a-zA-Z0-9]", check_element))

def validate_pw(pw): # 비밀번호 유효성 검사
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


def main(request):  # 시작 메인 페이지
    return render(request,'login.html')

def join(request):  # 회원가입
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['pwd']
        password2 = request.POST['pwdcheck']
        username = request.POST['username']
        if password1 == password2:
            try:
                user = User.objects.create_user(username = username, password = password1, email = email)     
                auth.login(request, user)
                return redirect('../keyword')
            except Exception as e:
                print(e)
                messages.info(request, e)
        else : 
            print("incorrect")
            messages.info(request, "check your password!!!")
        
    return render(request,'join.html')
            

def keyword(request): # 키워드 선택
    if request.method == 'POST':
        if request.user.is_authenticated:
            user_id = request.user.id
            print(user_id)
            keywords = []
            selected = request.POST.getlist('keyword[]')
            for i in selected :
                keywords.append(int(i))  
            try:
                cursor = connection.cursor()
                for i in keywords:
                    cursor.execute("insert into keyword_user values(%s ,%s)", [i, user_id])

                connection.commit()
                connection.close()
                return render(request,'index.html')
            
            except Exception as ex:
                print("Filed selecting in BookListView")
                raise ex
                      
       
    return render(request,'keyword.html')



def success(request):
    if request.method == 'POST':
        login = request.POST.getlist('keyword[]')
        print(login)
    return render(request, 'success.html')




def login(request):
    if request.user.is_authenticated:
        return redirect("./index")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pwd']
        print(username, password)

        user = auth.authenticate(request, username=username, password=password)

        if user is not None :
            auth.login(request, user)
            print("ok")
            return redirect('./index')
        else :
            print("nono")
            return render(request, 'login.html', {'error' : 'username or password is incorrect'})
    else :
        return render(request, 'login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("./")
    return render(request, 'login.html')




def api(request):
    videos = []
    videos_music = []
    if request.method == 'POST':
        if request.user.is_authenticated:
            search_url = 'https://www.googleapis.com/youtube/v3/search'
            video_url = 'https://www.googleapis.com/youtube/v3/videos'

            search_params = {
                'part' : 'snippet',
                'q' : request.POST['search'],
                'key' : my_settings.YOUTUBE_API['YOUTUBE_API_KEY'],
                'maxResults' : 20,
                'type' : 'video'
            }

            search_music_params = {
                    'part' : 'snippet',
                    'q' : request.POST['search'],
                    'key' : my_settings.YOUTUBE_API['YOUTUBE_API_KEY'],
                    'maxResults' : 20,
                    'type' : 'video',
                    'videoCategoryId' : '10'
                }


            r = requests.get(search_url, params=search_params)
            r_music = requests.get(search_url, params=search_music_params)
            results = r.json()['items']
            results_music = r_music.json()['items']


            video_ids = []
            video_music_ids = []

            for result in results :
                video_ids.append(result['id']['videoId'])

            for result in results_music :
                video_music_ids.append(result['id']['videoId'])

            if request.POST['submit'] == 'lucky' :
                return redirect(f'https://www.youtube.com/watch?v={ video_ids[0] }')

            if request.POST['submit'] == 'logout':
                    auth.logout(request)
                    return redirect('/start')


            video_params = {
                'key' : my_settings.YOUTUBE_API['YOUTUBE_API_KEY'],
                'part' : 'snippet, contentDetails',
                'id' : ','.join(video_ids),
                'maxResults' : 20
            }

            video_music_params = {
                'key' : my_settings.YOUTUBE_API['YOUTUBE_API_KEY'],
                'part' : 'snippet, contentDetails',
                'id' : ','.join(video_music_ids),
                'maxResults' : 20
            }

            r = requests.get(video_url, params=video_params)
            r_music = requests.get(video_url, params=video_music_params)

            results = r.json()['items']
            music_results = r_music.json()['items']

            for result in results :
                video_data = {
                    'title' : result['snippet']['title'],
                    'id' : result['id'],
                    'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                    'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                    'thumbnail' : result['snippet']['thumbnails']['high']['url']
                }

                videos.append(video_data)
                

            for result in music_results :
                video_music_data = {
                    'title' : result['snippet']['title'],
                    'id' : result['id'],
                    'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                    'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                    'thumbnail' : result['snippet']['thumbnails']['high']['url']
                }
                print(video_music_data)
                videos_music.append(video_music_data)
    
    movies = movie(request)

    context = {
        'videos' : videos,
        'videos_music' : videos_music,
        'movies' :  movies
    }

    return render(request, 'index.html', context)



def movie(request):
    movies = []
    if request.method == 'POST':
        if request.user.is_authenticated:
            config_secret_debug = my_settings.NAVER
            client_id = config_secret_debug['CLIENT_ID']
            client_secret = config_secret_debug['CLIENT_SECRET']

            q = request.POST['search']
          
            if (q == None) :
                return render(request,'result.html')
            else:
                encText = urllib.parse.quote("{}".format(q))
                url = "https://openapi.naver.com/v1/search/movie?query=" + encText  # json 결과
                movie_api_request = urllib.request.Request(url)
                movie_api_request.add_header("X-Naver-Client-Id", client_id)
                movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
                response = urllib.request.urlopen(movie_api_request)
                rescode = response.getcode()
                if (rescode == 200):
                    response_body = response.read()
                    result = json.loads(response_body.decode('utf-8'))
                    results = result.get('items')
                  
                    for result in results :
                        video_data = {
                            'title' : result['title'],
                            'image' : result['image'],
                            'url' : result['link'],
                            'pubDate' : result['pubDate'],
                            'userRating' : result['userRating'] ,
                            'director' : result['director'],
                            'actor' : result['actor']
                        }
                        print(video_data)
                        movies.append(video_data)   
    return movies
    #return render(request, 'result.html', {"movies" : movies})