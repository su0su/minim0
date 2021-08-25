from django.shortcuts import render
from django.shortcuts import render, redirect
import my_settings
import requests
from isodate import parse_duration
import json
import urllib.request

# Create your views here.
def api(request):
    videos = []
    videos_music = []
    if request.method == 'POST':
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
    return movies
    #return render(request, 'result.html', {"movies" : movies})