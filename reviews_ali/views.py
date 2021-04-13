from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import News, Reviews
from .forms import FeedbacksForm

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

class VideoView(ListView):
    model = Reviews
    queryset = Reviews.objects.all()
    template_name = 'reviews_ali/video.html'


class VideoDetaillView(DetailView):
    model = Reviews
    slug_field = 'url'
    template_name = 'reviews_ali/video_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FeedbacksForm()
        return context

class SearchVideo(ListView):
    template_name = 'reviews_ali/video.html'

    def get_queryset(self):
        return Reviews.objects.filter(title__icontains=self.request.GET.get('search_video'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search_video'] = f'searchvideo={self.request.GET.get("search_video")}&'
        return context

class AddFeedback(View):
    def post(self, request, pk):
        form = FeedbacksForm(request.POST)
        video = Reviews.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.video = video
            form.save()
        return redirect(video.get_absolute_url())

class AddFeedbackNews(View):
    def post(self, request, pk):
        form = FeedbacksForm(request.POST)
        news = News.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.news = news
            form.save()
        return redirect(news.get_absolute_url())