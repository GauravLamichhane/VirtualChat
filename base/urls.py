from django.urls import path,include
from . import views



urlpatterns = [
  path('login/',views.loginpage,name = 'login'),
  path('logout/',views.logoutUser,name = 'logout'),
  path('register/',views.registerPage,name = 'register'),
  path('',views.home,name='home'),
  path('room/<int:pk>/',views.room, name='room'),
  path('profile/<int:pk>/',views.userProfile, name='user-profile'),
  path('create-room/',views.createRoom, name='create-room'),
  path('update-room/<int:pk>/',views.updateRoom,name='update-room'),
  path('delete-room/<int:pk>/',views.deleteRoom,name='delete-room'),
  path('delete-message/<int:pk>/',views.deleteMessage,name='delete-message'),
  path('update-user/',views.updateUser,name='update-user'),
  path('topics/',views.topicsPage,name='topics'),
  path('activity/',views.activityPage,name='activity'),
]