from django.shortcuts import render
from .forms import YoutubeForm
from .models import YoutubeScrap, Youtube, KeywordYoutube, Keyword, Music, Movie, Playlist
from django.db import connection
# Create your views here.
def index(request):
    return render(request, './shareyourtaste.html')

def youtube_input(request): # 영상 넣기
    print("db")
    title = "ASTRO(아스트로), THE SHOW CHOICE! [THE SHOW 210810]"
    y_id = 'Gglh_fz9HP8'
    url = 'https://www.youtube.com/watch?v=Gglh_fz9HP8'
    duration = 3
    thumbnail = 'https://i.ytimg.com/vi/Gglh_fz9HP8/hqdefault.jpg'
    content = 1
    writer = 6
    keywords = ["아이돌", "댄스"]
    try:
        cursor = connection.cursor()
        #cursor.execute("insert into youtube(title, y_id, url, duration, thumbnail, content, writer) values(%s ,%s, %s, %s, %s, %s, %s)", [title, y_id, url, duration, thumbnail, content, writer])
        print(Youtube.objects.filter(y_id=y_id, writer = writer).order_by('-id')[0].id)
        youtube_id = Youtube.objects.filter(y_id=y_id, writer = writer).order_by('-id')[0].id
        for key in keywords :
            print(Keyword.objects.get(name = key).id)
            key_id=Keyword.objects.get(name = key).id
            #cursor.execute("insert into keyword_youtube values(%s, %s)", [key_id, youtube_id])     
        
      
        connection.commit()
        connection.close()

    
    except Exception as ex:
        print("Filed selecting in BookListView")
        raise ex

    return render(request, './db.html')


def music_input(request): # 음악 넣기
    title = 'Naomi Scott - Speechless ( cover by J.Fla )'
    y_id = 'S8e1geEpnTA'
    url = 'https://www.youtube.com/watch?v=S8e1geEpnTA'
    duration = 3
    thumbnail = 'https://i.ytimg.com/vi/S8e1geEpnTA/hqdefault.jpg'
    content = 2
    writer = 6
    keywords = ["커버", "OST"]
    try:
        cursor = connection.cursor()
        #cursor.execute("insert into music(title, y_id, url, duration, thumbnail, content, writer) values(%s ,%s, %s, %s, %s, %s, %s)", [title, y_id, url, duration, thumbnail, content, writer])
        print(Music.objects.filter(y_id=y_id, writer = writer).order_by('-id')[0].id)
        music_id = Music.objects.filter(y_id=y_id, writer = writer).order_by('-id')[0].id
        for key in keywords :
            print(Keyword.objects.get(name = key).id)
            key_id=Keyword.objects.get(name = key).id
            #cursor.execute("insert into keyword_music values(%s, %s)", [key_id, music_id])     
              
        connection.commit()
        connection.close()

    
    except Exception as ex:
        print("Filed selecting in BookListView")
        raise ex

    return render(request, './db.html')

def movie_input(request): # 영화 넣기
    title = '캡틴 <b>마블</b> 2'
    url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=196366'
    rating = '0.00'
    thumbnail = 'https://ssl.pstatic.net/imgmovie/mdi/mit110/1963/196366_P01_123229.jpg'
    content = 1
    writer = 6
    director = '니아 다코스타|'
    actor = '브리 라슨|테요나 패리스|이만 벨라니|'
    keywords = ["액션", "어드벤쳐"]
    try:
        cursor = connection.cursor()
        #cursor.execute("insert into movie(title, url,thumbnail, content, writer, actor, rating, director) values(%s ,%s, %s, %s, %s, %s, %s, %s)", [title, url,thumbnail, content, writer, actor, rating, director])
        print(Movie.objects.filter(title=title, writer = writer, director=director).order_by('-id')[0].id)
        movie_id = Movie.objects.filter(title=title, writer = writer, director=director).order_by('-id')[0].id
        for key in keywords :
            print(Keyword.objects.get(name = key).id)
            key_id=Keyword.objects.get(name = key).id
            #cursor.execute("insert into keyword_movie values(%s, %s)", [key_id, movie_id])     
        
      
        connection.commit()
        connection.close()

    
    except Exception as ex:
        print("Filed selecting in BookListView")
        raise ex

    return render(request, './db.html')
 
def playlist_input(request):
    title = 'Will Smith - Prince Ali (From "Aladdin")'
    starter = 6
    content = 2
    url = 'https://www.youtube.com/watch?v=eGLSPyGszjo'
    thumbnail = 'https://i.ytimg.com/vi/eGLSPyGszjo/hqdefault.jpg'
    keywords = ["OST", "판타지"]

    try:
        cursor = connection.cursor()
        #cursor.execute("insert into playlist(title, starter, content) values(%s ,%s, %s)", [title, starter, content])
        print(Playlist.objects.filter(title=title, starter = starter, content = content).order_by('-id')[0].id)
        playlist_id = Playlist.objects.filter(title=title, starter = starter, content = content).order_by('-id')[0].id
        for key in keywords :
            print(Keyword.objects.get(name = key).id)
            key_id=Keyword.objects.get(name = key).id
            #cursor.execute("insert into keyword_playlist values(%s, %s)", [key_id, playlist_id])     
        #cursor.execute("insert into playlist_contents(writer, content, playlist, title, thumbnail, url) values(%s ,%s, %s, %s, %s, %s)", [starter, content, playlist_id, title, thumbnail, url])
      
        connection.commit()
        connection.close()

    
    except Exception as ex:
        print("Filed selecting in BookListView")
        raise ex
    return render(request, './db.html')

def sub_playlist_input(request):
    
    title = 'Sunghwa Chung - 아라비안 나이트 (2019) (From “알라딘”)'
    writer = 6
    content = 2
    url = 'https://www.youtube.com/watch?v=XWxU2bSLs3s'
    thumbnail = 'https://i.ytimg.com/vi/XWxU2bSLs3s/hqdefault.jpg'
    playlist_id = 3

    try:
        cursor = connection.cursor()
        cursor.execute("insert into playlist_contents(writer, content, playlist, title, thumbnail, url) values(%s ,%s, %s, %s, %s, %s)", [writer, content, playlist_id, title, thumbnail, url])
      
        connection.commit()
        connection.close()

    
    except Exception as ex:
        print("Filed selecting in BookListView")
        raise ex
    return render(request, './db.html')


