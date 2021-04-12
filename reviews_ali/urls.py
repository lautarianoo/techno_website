from django.urls import path
from .views import Index, NewsDetailView, SearchFilm

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('news/<slug:slug>', NewsDetailView.as_view(), name='news_detail'),
    path('searchnews/', SearchFilm.as_view(), name='search_news')
]