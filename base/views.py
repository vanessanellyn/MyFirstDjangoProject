from django.shortcuts import render
from base.models import Room

# Views may be functions or classes
# Views will also relay our request to any database or templates
# Create your views here.


def home(request):
    rooms = Room.objects.all()
    return render(request, "base/home.html", {'rooms': rooms})


def room(request, pk):
    room = Room.objects.get(id=pk)
    return render(request, "base/room.html", {'room': room})
