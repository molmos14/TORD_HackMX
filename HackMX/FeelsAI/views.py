from django.shortcuts import render
from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
    return HttpResponse("Hello World")

def random(request):
    movies = Movie.objects.filter(release_year=2014)
    for movie in movies:
        print(movie.title)