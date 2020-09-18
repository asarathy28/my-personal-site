from django.shortcuts import render
from .models import WritingPost

# Create your views here.
def home(response):
    return render(response, "main/home.html", {})

def writing(response):
    #pieces = WritingPost.objects.get(title="Seen in the Sun")
    return render(response, "main/writing.html", {}) #{"pieces":pieces})

def running(response):
    return render(response, "main/running.html", {})

def csProjects(response):
    return render(response, "main/cs-projects.html", {})

def resume(response):
    return render(response, "main/resume.html", {})

#writing
def seenInTheSun(response):
    return render(response, "main/writing/seen-in-the-sun.html", {})

def softWords(response):
    return render(response, "main/writing/soft-words.html", {})
