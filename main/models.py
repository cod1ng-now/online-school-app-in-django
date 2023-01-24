from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Playlist(models.Model):
    nomi = models.CharField(max_length=150)
    image = models.ImageField(upload_to = 'rasmlar/playlist_rasm')
    sana = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nomi

    
class VideoDars(models.Model):
    nomi = models.CharField(max_length=150)
    rasm = models.ImageField(upload_to='video_darslar/rasmlar')
    izoh = models.TextField()
    video = models.FileField(upload_to='video_darslar/video')
    playlisti = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    # sana = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.nomi
    
    
# class Teachers(models.Model):
#     ismi = models.CharField(max_length=150)
#     rasmi = models.ImageField(upload_to = 'teachers/rasmi')
    