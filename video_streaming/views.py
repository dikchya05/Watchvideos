from django.shortcuts import render
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
