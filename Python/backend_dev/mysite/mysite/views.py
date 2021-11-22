# created by me -Soumya
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello soumya</h1>")


def about(request):
    return HttpResponse("Hello soumya this is about section")


def image(request):
    return HttpResponse("<img src='images2.png' alt='Girl in a jacket' width='500' height='600'>")