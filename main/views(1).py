from django.shortcuts import render
from .models import Playlist, VideoDars
from django.views.generic import DetailView
# Create your views here.


def index(request):
    playlistlar = Playlist.objects.all()
    return render(request, 'index.html', {'playlistlar':playlistlar})


def post(request):
    return render(request, 'video.html')

def darslar(request):
    playlistlar = Playlist.objects.all()
    return render(request, 'darslar.html', {'playlistlar':playlistlar})

def teachers(request):
    return render(request, 'teachers.html')

def bizhaqimizda(request):
    return render(request, 'bizhaqimizda.html')


def aloqa(request):
    return render(request, 'contact.html')

class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'playlist.html'
    context_object_name = 'playlist'
    
    
    
class VideoDarsDetailView(DetailView):
    model = VideoDars
    template_name = 'video.html'
    context_object_name = 'video'
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["videolar"] = VideoDars.objects.all()
        return context
        