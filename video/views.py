from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Video
from .forms import VideoForm
from django.contrib.auth.decorators import login_required
from .models import Video, Like, Dislike, Comment
from .forms import CommentForm

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

# def recommended_videos(request):
#     videos = Video.objects.all().order_by('-created_at')[:10]  # Show latest 10 videos
#     return render(request, 'video/recommended_videos.html', {'videos': videos})

def video_detail(request, video_id):
    # Get the specific video by ID
    video = get_object_or_404(Video, id=video_id)
    # Get all comments related to this video
    comments = Comment.objects.filter(video=video).order_by('-created_at')
   

    # Create a new comment form
    form = CommentForm()

  # If the request is a POST (i.e., submitting a comment)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.video = video
            comment.user = request.user
            comment.save()
            return redirect('video_detail', video_id=video.id)  # Refresh the page

    return render(request, 'video/video_detail.html', {
        'video': video,
        'comments': comments,
        'form': form
    })
    
    
    
    # Render the detail page with the video data
    # return render(request, 'video/video_detail.html', {'video': video})

def user_video_detail(request, video_id):
    # Get the specific video by ID
    video = get_object_or_404(Video, id=video_id)
    comments = Comment.objects.filter(video=video).order_by('-created_at')
   

    # Create a new comment form
    form = CommentForm()

  # If the request is a POST (i.e., submitting a comment)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.video = video
            comment.user = request.user
            comment.save()
            return redirect('video_detail', video_id=video.id) 
        # Refresh the page
    return render(request, 'video/video_detail.html', {
        'video': video,
        'comments': comments,
        'form': form
    })



@login_required
def like_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    existing_dislike = Dislike.objects.filter(user=request.user, video=video)

    # Remove dislike if user previously disliked
    if existing_dislike.exists():
        existing_dislike.delete()

    # Check if user already liked
    if not Like.objects.filter(user=request.user, video=video).exists():
        Like.objects.create(user=request.user, video=video)

    return redirect('video_detail', video_id=video.id)

@login_required
def dislike_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    existing_like = Like.objects.filter(user=request.user, video=video)

    # Remove like if user previously liked
    if existing_like.exists():
        existing_like.delete()

    # Check if user already disliked
    if not Dislike.objects.filter(user=request.user, video=video).exists():
        Dislike.objects.create(user=request.user, video=video)

    return redirect('video_detail', video_id=video.id)

@login_required
def add_comment(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == "POST":
        content = request.POST.get("content")
        Comment.objects.create(video=video, user=request.user, content=content)
    return redirect("video_detail", video_id=video_id)


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Allow only the comment owner or admin to delete
    if request.user == comment.user or request.user.is_superuser:
        comment.delete()
    
    return redirect(request.META.get('user_video_details', 'home'))
