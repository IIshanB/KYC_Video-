from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from recorder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('play/<int:video_id>/',views.play_video, name='play_video'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
