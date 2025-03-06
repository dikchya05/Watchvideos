from django.urls import path, include
from .views import register, user_login
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    # path('home/', include('video_streaming.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

