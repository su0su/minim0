from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from isodate import parse_duration
import my_settings
from django.contrib.auth.models import User
import requests
from django.contrib import auth
import urllib.request
import json
from bs4 import BeautifulSoup
from multiprocessing import Pool, process


# Create your views here.
def show(request):
    return render(request, 'result.html')
    #return HttpResponse("Hello, world. You're at the polls index.")



def youtube(request):

    if request.user.is_authenticated:
        user_info = request.user.username
        print("d : ", request.user.username)
        videos = []
        if request.method == 'POST':
            search_url = 'https://www.googleapis.com/youtube/v3/search'
            video_url = 'https://www.googleapis.com/youtube/v3/videos'
            video_categories = 'https://www.googleapis.com/youtube/v3/videoCategories'

            search_params = {
                'part' : 'snippet',
                'q' : request.POST['search'],
                'key' : my_settings.YOUTUBE_API['YOUTUBE_API_KEY'],
                'maxResults' : 20,
                'type' : 'video',
                'videoCategoryId' : '10'
            }

            r = requests.get(search_url, params=search_params)
            results = r.json()['items']

            video_ids = []
            for result in results :
                video_ids.append(result['id']['videoId'])
                

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

            r = requests.get(video_url, params=video_params)
            
            results = r.json()['items']

            for result in results :
                video_data = {
                    'title' : result['snippet']['title'],
                    'id' : result['id'],
                    'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                    'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                    'thumbnail' : result['snippet']['thumbnails']['high']['url']
                }

                videos.append(video_data)


        context = {
            'results' : videos,
            'user' : user_info
        }
    else :
        return redirect("/start")

    return render(request, 'result.html', context)



# Create your views here.
def music(request):  
    global results
    results = []
    if request.method == 'POST': 

        config_secret_debug = my_settings.LAST
        api_key = config_secret_debug['API_KEY']

        q = request.POST['search']
        if (q == None) :
            return redirect("/start")
        else:
            encText = urllib.parse.quote("{}".format(q))
            print(encText)
            url = "http://ws.audioscrobbler.com/2.0/?method=track.search&track=" + encText + "&api_key=" +api_key+ "&format=json"# json 결과
            response = urllib.request.urlopen(url)

            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            print(result)
            results = result['results']['trackmatches']['track']


        #이미지 크롤링
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        artist_url=[]
        for i in range(0,len(results)):
            artist_url.append(results[i]['url'])

        for i in range(0,len(artist_url)):
            html=urllib.request.urlopen(artist_url[i])
            result=BeautifulSoup(html.read(),"html.parser")
            
            try:
                artist_img=result.find('span',{'class':'cover-art'}).find('img')
                path=artist_img.get("src") # 파일 경로
                results[i]['image'] = path
            except:
                pass
    print(results)
            
    return render(request, 'result.html', { 'results' : results })


    
   
    

def movie(request):
    movies = []
    if request.method == 'POST':

        config_secret_debug = my_settings.NAVER
        client_id = config_secret_debug['CLIENT_ID']
        client_secret = config_secret_debug['CLIENT_SECRET']

        q = request.POST['search']
        print(q)
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
                print(results)
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

    return render(request, 'result.html', {"movies" : movies})