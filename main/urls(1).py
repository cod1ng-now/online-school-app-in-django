from django.urls import path
from .views import index, post, darslar, teachers, bizhaqimizda, aloqa, PlaylistDetailView, VideoDarsDetailView


urlpatterns = [
    path('', index, name='index'),
    path('video/', post, name='post'),
    path('darslar/', darslar, name='darslar'),
    path('video/<int:pk>/', VideoDarsDetailView.as_view(), name='video'),
    path('playlist-vid/<int:pk>/', PlaylistDetailView.as_view(), name='playlist-detail'),
    path('teachers/', teachers, name='yangiliklar'),
    path('bizhaqimizda/', bizhaqimizda, name='bizhaqimizda'),
    path('aloqa/', aloqa, name='aloqa')
]