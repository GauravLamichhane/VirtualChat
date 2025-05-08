from django.shortcuts import render

rooms = [
  {'id': 1, 'name':'Learnpython'},
  {'id': 2, 'name':'FrontEnd'},
]

def home(request):
  return render(request,'home.html',{'rooms':rooms})

def room(request):
  return render(request,'room.html')