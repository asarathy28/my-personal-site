from django.shortcuts import render
#from .models import ContactMessage
from .forms import ContactForm

# Create your views here.
def home(request):

    form = ContactForm()

    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, "main/home.html", context)

def writing(request):
    #pieces = WritingPost.objects.get(title="Seen in the Sun")
    return render(request, "main/writing.html", {}) #{"pieces":pieces})

def running(request):
    return render(request, "main/running.html", {})

def csProjects(request):
    return render(request, "main/cs-projects.html", {})



#writing
def seenInTheSun(request):
    return render(request, "main/writing/seen-in-the-sun.html", {})

def softWords(request):
    return render(request, "main/writing/soft-words.html", {})

def browniesAndWhiskey(request):
    return render(request, "main/writing/brownies-and-whiskey.html", {})

def beyondTheWall(request):
    return render(request, "main/writing/beyond-the-wall.html", {})

def goneGirl(request):
    return render(request, "main/writing/gone-girl.html", {})

#running
