from django.shortcuts import render
from django.shortcuts import render, redirect
import my_settings
import requests
from isodate import parse_duration

# Create your views here.
def youtubeapi(request):
    videos = []
    if request.method == 'POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
            'part' : 'snippet',
            'q' : request.POST['search'],
            'key' : my_settings.YOUTUBE_API['YOUTUBE_API_KEY'],
            'maxResults' : 10,
            'type' : 'video'
        }


        r = requests.get(search_url, params=search_params)
        results = r.json()['items']


        video_ids = []
        for result in results :
            video_ids.append(result['id']['videoId'])

        if request.POST['submit'] == 'lucky' :
            return redirect(f'https://www.youtube.com/watch?v={ video_ids[0] }')


        video_params = {
            'key' : my_settings.YOUTUBE_API['YOUTUBE_API_KEY'],
            'part' : 'snippet, contentDetails',
            'id' : ','.join(video_ids),
            'maxResults' : 10
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
    }

    return render(request, 'index.html', context)