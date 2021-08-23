from django.conf import settings
from django.shortcuts import render, redirect
from isodate import parse_duration
import my_settings
from django.contrib.auth.models import User
import requests
from django.contrib import auth

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

            search_params = {
                'part' : 'snippet',
                'q' : request.POST['search'],
                'key' : my_settings.YOUTUBE_API['YOUTUBE_API_KEY'],
                'maxResults' : 9,
                'type' : 'video'
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
                'maxResults' : 9
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
            'videos' : videos,
            'user' : user_info
        }
    else :
        return redirect("/start")

    return render(request, 'result.html', context)