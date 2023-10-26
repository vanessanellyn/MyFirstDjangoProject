from django.shortcuts import render

# Views may be functions or classes
# Views will also relay our request to any database or templates
# Create your views here.


def home(request):
  return render(request, "home.html")


def room(request):
  return render(request, "room.html")
