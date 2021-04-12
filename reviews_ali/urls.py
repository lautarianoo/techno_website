from django.urls import path
from .views import Index, NewsDetailView, SearchVideo, SearchFilm, VideoView, VideoDetaillView, AddFeedback

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('news/<slug:slug>', NewsDetailView.as_view(), name='news_detail'),
    path('searchnews/', SearchFilm.as_view(), name='search_news'),
    path('video/', VideoView.as_view(), name='video'),
    path('video-detail/<slug:slug>', VideoDetaillView.as_view(), name='video_detail'),
    path('searchvideo/', SearchVideo.as_view(), name='search_video'),
    path('addfeedback/<int:pk>', AddFeedback.as_view(), name='feedbackadd')
]