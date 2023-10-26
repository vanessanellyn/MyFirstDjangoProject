from django.http import HttpResponse
from django.shortcuts import render

# Views may be functions or classes
# Views will also relay our request to any database or templates
# Create your views here.


def home(request):
  return HttpResponse("hello world")


def room(request):
  return HttpResponse("ROOM")
