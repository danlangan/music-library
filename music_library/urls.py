from django.urls import path
from . import views

urlpatterns = [
    path('music_library/', views.song_list)
]