from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import like_video, dislike_video, delete_comment



urlpatterns = [
    path('videos/', views.video_list, name='video_list'),
    path('user-videos/', views.user_video_list, name='user_video_list'),
    path('videos/add/', views.add_video, name='add_video'),
    # path('videos/edit/<int:video_id>/', views.edit_video, name='edit_video'),
    # path('videos/delete/<int:video_id>/', views.delete_video, name='delete_video'),
    
    # path('videos/edit/<int:video_id>/', views.edit_video, name='edit_video'),
    # path('videos/delete/<int:video_id>/', views.delete_video, name='delete_video'),
    
    path('edit/<int:video_id>/', views.edit_video, name='edit_video'),  # Edit video page
    path('delete/<int:video_id>/', views.delete_video, name='delete_video'),  # Delete video
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),  # Video detail page
    path('user-video/<int:video_id>/', views.user_video_detail, name='user_video_detail'),  # Video detail page
    path('video/<int:video_id>/like/', like_video, name='like_video'),
    path('video/<int:video_id>/dislike/', dislike_video, name='dislike_video'),
    path("video/<int:video_id>/comment/", views.add_comment, name="add_comment"),
     path('comment/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
    # path('recommended/', recommended_videos, name='recommended_videos'),
   


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
