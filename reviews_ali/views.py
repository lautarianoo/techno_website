from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News

class Index(ListView):
    #Домашняя страница, список новостей
    model = News
    queryset = News.objects.all()
    template_name = 'reviews_ali/index.html'

class NewsDetailView(DetailView):
    model = News
    slug_field = 'url'
    template_name = 'reviews_ali/news_detail.html'

class SearchFilm(ListView):
    template_name = 'reviews_ali/index.html'

    def get_queryset(self):
        return News.objects.filter(title__icontains=self.request.GET.get('search_news'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search_news'] = f'searchnews={self.request.GET.get("search_news")}&'
        return context