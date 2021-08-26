from django import forms
from django.http import HttpResponse, HttpResponseRedirect

class YoutubeForm(forms.Form):
    title = forms.CharField()
    y_id = forms.CharField()
    url = forms.URLField()
    duration = forms.IntegerField()
    thumbnail = forms.CharField()
    scrap = forms.IntegerField()
    good = forms.IntegerField()
    content = forms.IntegerField()
    writer = forms.IntegerField()