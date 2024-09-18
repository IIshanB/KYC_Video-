from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('play/<int:video_id>/',views.play_video, name='play_video'),
]
