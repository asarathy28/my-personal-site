from django.shortcuts import render, redirect
#from .models import ContactMessage
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .spotify import User_Music



# Create your views here.
def home(request):

    form = ContactForm()

    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():

            name = request.POST['name']
            subject = request.POST['subject']
            message = request.POST['message']
            email =request.POST['email']


            context = {'subject':subject, 'message':message, 'name':name, 'email':email}
            template = render_to_string('main/email-temp.html', context)


            send_mail(f'{name} : {subject}', template, settings.EMAIL_HOST_USER, ['saraties2088@gmail.com'], fail_silently=False)

            send_mail(f'confirmation : {subject}', template, settings.EMAIL_HOST_USER, [request.POST['email']], fail_silently=False)

            form.save()

            return redirect('../confirmation/')
    else:  # 5
        # Create an empty form instance
        form = ContactForm()

    context = {'form':form}
    return render(request, "main/home.html", context)

def writing(request):
    #pieces = WritingPost.objects.get(title="Seen in the Sun")
    return render(request, "main/writing.html", {}) #{"pieces":pieces})

def running(request):
    return render(request, "main/running.html", {})

def music(request):
    myMusic = User_Music('1216336460')
    #'1216336460'

    #playlists = {'name':myMusic.pl_name, 'id':myMusic.pl_id, 'image':myMusic.pl_image}
    playlists = zip(myMusic.pl_name, myMusic.pl_id, myMusic.pl_image)

    return render(request, "main/music.html", {'playlists':playlists})

def csProjects(request):
    return render(request, "main/cs-projects.html", {})

def confirmation(request):
    return render(request, "main/confirmation.html", {})



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
