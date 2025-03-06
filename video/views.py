from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Video
from .forms import VideoForm

# Check if user is admin
def is_admin(user):
    return user.is_superuser

# @user_passes_test(is_admin)
def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'video/add_video.html', {'form': form})

# @user_passes_test(is_admin)
# def edit_video(request, video_id):
#     video = get_object_or_404(Video, id=video_id)
#     if request.method == 'POST':
#         form = VideoForm(request.POST, request.FILES, instance=video)
#         if form.is_valid():
#             form.save()
#             return redirect('video_list')
#     else:
#         form = VideoForm(instance=video)
#     return render(request, 'video/edit_video.html', {'form': form, 'video': video})


def edit_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('video_list')  # Redirect to the video list page after saving
    else:
        form = VideoForm(instance=video)

    return render(request, 'video/edit_video.html', {'form': form, 'video': video})

# @user_passes_test(is_admin)
# def delete_video(request, video_id):
#     video = get_object_or_404(Video, id=video_id)
#     if request.method == 'POST':
#         video.delete()
#         return redirect('video_list')
#     return render(request, 'video/delete_video.html', {'video': video})

def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        video.delete()
        return redirect('video_list')  # Redirect to the video list page after deletion

# @user_passes_test(is_admin)
def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video/video_list.html', {'videos': videos})

def user_video_list(request):
    videos = Video.objects.all()
    return render(request, 'video/user_video_list.html', {'videos': videos})

def video_detail(request, video_id):
    # Get the specific video by ID
    video = get_object_or_404(Video, id=video_id)
    
    # Render the detail page with the video data
    return render(request, 'video/video_detail.html', {'video': video})

def user_video_detail(request, video_id):
    # Get the specific video by ID
    video = get_object_or_404(Video, id=video_id)
    
    # Render the detail page with the video data
    return render(request, 'video/video_detail.html', {'video': video})
