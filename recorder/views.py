

# Create your views here.
from django.shortcuts import render
from .models import Video
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')
@csrf_exempt
def upload(request):
    if request.method == 'POST' and request.FILES.get('video'):
        video = request.FILES['video']
        # Save the video file to the media directory or database
        video = request.FILES['video']
        video_instance = Video.objects.create(title='KYC Video', video_file=video)

        return HttpResponse(f'Video uploaded successfully! Video ID: {video_instance.id}')
    return HttpResponse('Failed to upload video.', status=400)

def play_video(request, video_id):
    try:

        video = Video.objects.get(id=video_id)

        return render(request, 'play_video.html', {'video': video})
    except Video.DoesNotExist:
        return HttpResponse('Video not found.', status=404)