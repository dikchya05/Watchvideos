
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from video.models import Video


@login_required
def home(request):
    if request.user.is_authenticated:
        if request.user.role == 'admin':
            user_type = 'admin'
        else:
            user_type = 'normal'
    else:
        user_type = 'guest'  # Or any default logic

    return render(request, 'home.html', {'user_type': user_type})


def video_detail(request, id):
    video = get_object_or_404(Video, id=id)  # Fetch the video by ID
    return render(request, 'video_detail.html', {'video': video})