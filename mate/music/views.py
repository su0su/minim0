from django.http import HttpResponse
import urllib.request
import json
import my_settings

from django.shortcuts import render

#def show(request):
    #return render(request, 'songsearch.html')

# Create your views here.
def music(request):  
    if request.method == 'GET':

        config_secret_debug = my_settings.LAST
        api_key = config_secret_debug['API_KEY']

        q = request.GET.get('q')
        encText = urllib.parse.quote("{}".format(q))
        url = "http://ws.audioscrobbler.com/2.0/?method=artist.search&artist=" + encText + "&api_key=" +api_key+ "&format=json"# json 결과
        response = urllib.request.urlopen(url)

        response_body = response.read()
        result = json.loads(response_body.decode('utf-8'))
        results = result['results']['artistmatches']['artist']
        print(results)
        context = {
            'results': results
        }

        return render(request, 'music/songsearch.html', context=context)