from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('writing/', views.writing, name='writing'),
    path('running/', views.running, name='running'),
    path('cs-projects/', views.csProjects, name='cs-prjoects'),
    path('resume/', views.resume, name='resume'),

    path('seen-in-the-sun/', views.seenInTheSun, name='seen-in-the-sun'),
    path('soft-words/', views.softWords, name='soft-words')
]
