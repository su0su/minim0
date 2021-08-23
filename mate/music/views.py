from django.conf.urls import url
from django.http import HttpResponse
from bs4 import BeautifulSoup
from django.shortcuts import render
import urllib.request
import json
import my_settings

from urllib import request
    

# Create your views here.
def music(request):  
    if request.method == 'GET':

        config_secret_debug = my_settings.LAST
        api_key = config_secret_debug['API_KEY']

        q = request.GET.get('q')
        if (q == None) :
            return render(request,'music/songsearch.html')
        else:
            encText = urllib.parse.quote("{}".format(q))
            url = "http://ws.audioscrobbler.com/2.0/?method=track.search&track=" + encText + "&api_key=" +api_key+ "&format=json"# json 결과
            response = urllib.request.urlopen(url)

            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
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
                results[i]['url'] = path
            except:
                pass

#songsearch.html로 값 전달
        context = {
            'results': results
        }

        return render(request, 'music/songsearch.html', context=context)
