from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('writing/', views.writing, name='writing'),
    path('running/', views.running, name='running'),
    path('music/', views.music, name='music'),
    path('cs-projects/', views.csProjects, name='cs-prjoects'),

    path('seen-in-the-sun/', views.seenInTheSun, name='seen-in-the-sun'),
    path('soft-words/', views.softWords, name='soft-words'),
    path('brownies-and-whiskey/', views.browniesAndWhiskey, name='brownies-and-whiskey'),
    path('beyond-the-wall/', views.beyondTheWall, name='beyond-the-wall'),
    path('gone-girl/', views.goneGirl, name='gone-girl'),

    path('confirmation/', views.confirmation, name='confirmation'),
]
