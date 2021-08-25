from django.shortcuts import render
from .models import Keyword, KeywordUser, AuthUser
from django.db import connection
from youtube.views import movie
import my_settings
import requests
from isodate import parse_duration
import json
import urllib.request

# Create your views here.


def sign_up_keyword(request): #회원가입
    if request.user.is_authenticated:
        user_info = request.user.id
        print(user_info)
        if request.method == 'POST':
            selected = request.POST.getlist('keyword[]')
        keywords = []
        for i in selected :
            keywords.append(int(i))
        
        
        try:
            cursor = connection.cursor()
            for i in keywords:
                cursor.execute("insert into keyword_user values(%s ,%s)", [i, user_info])

            connection.commit()
            connection.close()
        
        except Exception as ex:
            print("Filed selecting in BookListView")
            raise ex

    return render(request, 'insert.html')


def upload_contents(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            contents_type = "music"
            search = "bts" #request.POST['search']
            search_url = 'https://www.googleapis.com/youtube/v3/search'
            video_url = 'https://www.googleapis.com/youtube/v3/videos'

            if contents_type == "music" :
                print("music")
                videos_music = []
                search_music_params = {
                    'part' : 'snippet',
                    'q' : search,
                    'key' : my_settings.YOUTUBE_API['YOUTUBE_API_KEY'],
                    'maxResults' : 20,
                    'type' : 'video',
                    'videoCategoryId' : '10'
                }
                r_music = requests.get(search_url, params=search_music_params)
                results_music = r_music.json()['items']
                video_music_ids = []       

                for result in results_music :
                    video_music_ids.append(result['id']['videoId'])

                video_music_params = {
                    'key' : my_settings.YOUTUBE_API['YOUTUBE_API_KEY'],
                    'part' : 'snippet, contentDetails',
                    'id' : ','.join(video_music_ids),
                    'maxResults' : 20
                }

                r_music = requests.get(video_url, params=video_music_params)

                music_results = r_music.json()['items']

                for result in music_results :
                    video_music_data = {
                        'title' : result['snippet']['title'],
                        'id' : result['id'],
                        'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                        'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                        'thumbnail' : result['snippet']['thumbnails']['high']['url']
                    }

                    videos_music.append(video_music_data)

            elif contents_type == "movie" :
                print("movie")
                movies = []
    

                config_secret_debug = my_settings.NAVER
                client_id = config_secret_debug['CLIENT_ID']
                client_secret = config_secret_debug['CLIENT_SECRET']

                q = search

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
                            
                            movies.append(video_data)   

            elif contents_type == "youtube" :
                print("youtube")
                videos = []
                search_params = {
                    'part' : 'snippet',
                    'q' : search,
                    'key' : my_settings.YOUTUBE_API['YOUTUBE_API_KEY'],
                    'maxResults' : 20,
                    'type' : 'video'
                }
                r = requests.get(search_url, params=search_params)
                results = r.json()['items']
                video_ids = []
                for result in results :
                    video_ids.append(result['id']['videoId'])

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



def test_content_insert_music(request):
    if request.user.is_authenticated:
        user_info = request.user.id
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'
        videos_music = []
        search_music_params = {
            'part' : 'snippet',
            'q' : 'bts',
            'key' : my_settings.YOUTUBE_API['YOUTUBE_API_KEY'],
            'maxResults' : 20,
            'type' : 'video',
            'videoCategoryId' : '10'
        }
        r_music = requests.get(search_url, params=search_music_params)
        results_music = r_music.json()['items']
        video_music_ids = []       

        for result in results_music :
            video_music_ids.append(result['id']['videoId'])

        video_music_params = {
            'key' : my_settings.YOUTUBE_API['YOUTUBE_API_KEY'],
            'part' : 'snippet, contentDetails',
            'id' : ','.join(video_music_ids),
            'maxResults' : 20
        }

        r_music = requests.get(video_url, params=video_music_params)

        music_results = r_music.json()['items']

        for result in music_results :
            video_music_data = {
                'title' : result['snippet']['title'],
                'id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail' : result['snippet']['thumbnails']['high']['url']
            }

            videos_music.append(video_music_data)
        i = videos_music[0]
        print(i["title"])
       
        if request.method == 'POST':
            search_url = 'https://www.googleapis.com/youtube/v3/search'
            video_url = 'https://www.googleapis.com/youtube/v3/videos'
            videos_music = []
            search_music_params = {
                'part' : 'snippet',
                'q' : 'bts',
                'key' : my_settings.YOUTUBE_API['YOUTUBE_API_KEY'],
                'maxResults' : 20,
                'type' : 'video',
                'videoCategoryId' : '10'
            }
            r_music = requests.get(search_url, params=search_music_params)
            results_music = r_music.json()['items']
            video_music_ids = []       

            for result in results_music :
                video_music_ids.append(result['id']['videoId'])

            video_music_params = {
                'key' : my_settings.YOUTUBE_API['YOUTUBE_API_KEY'],
                'part' : 'snippet, contentDetails',
                'id' : ','.join(video_music_ids),
                'maxResults' : 20
            }

            r_music = requests.get(video_url, params=video_music_params)

            music_results = r_music.json()['items']

            for result in music_results :
                video_music_data = {
                    'title' : result['snippet']['title'],
                    'id' : result['id'],
                    'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                    'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                    'thumbnail' : result['snippet']['thumbnails']['high']['url']
                }

                videos_music.append(video_music_data)
                i = videos_music[0]
                print(i)

            
            try:
                cursor = connection.cursor()
                #cursor.execute("insert into music values(%s ,%s, %s, %s, %s, %s, %s, %s, %s, %s)", [i, user_info])

                connection.commit()
                connection.close()
            
            except Exception as ex:
                print("Filed selecting in BookListView")
                raise ex


    return render(request,'keyword.html')