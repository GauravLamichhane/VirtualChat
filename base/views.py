from django.shortcuts import render

# rooms = [
#   {'id': 1, 'name':'Learn python'},
#   {'id': 2, 'name':'Front End'},
#   {'id':3,'name':'React Native'}
# ]
from .models import Room
def home(request):
  rooms = Room.objects.all()
  context = {'rooms':rooms}
  return render(request,'base/home.html',context)

def room(request,pk):
  room = Room.objects.get(id = pk)
  context = {'room':room}
  return render(request,'base/room.html',context)