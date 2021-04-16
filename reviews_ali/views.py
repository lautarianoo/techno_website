from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import News, Reviews, Aliexpress, Category
from .forms import FeedbacksForm

class Categor:
    """Жанры и года выхода фильмов"""
    def get_category(self):
        return Category.objects.all()

class Index(Categor, ListView):
    #Домашняя страница, список новостей
    model = News
    queryset = News.objects.all()
    template_name = 'reviews_ali/index.html'

class NewsDetailView(Categor,DetailView):
    model = News
    slug_field = 'url'
    template_name = 'reviews_ali/news_detail.html'

class SearchFilm(Categor,ListView):
    template_name = 'reviews_ali/index.html'

    def get_queryset(self):
        return News.objects.filter(title__icontains=self.request.GET.get('search_news'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search_news'] = f'searchnews={self.request.GET.get("search_news")}&'
        return context

class VideoView(Categor, ListView):
    model = Reviews
    queryset = Reviews.objects.all()
    template_name = 'reviews_ali/video.html'


class VideoDetaillView(Categor, DetailView):
    model = Reviews
    slug_field = 'url'
    template_name = 'reviews_ali/video_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FeedbacksForm()
        return context

class SearchVideo(Categor, ListView):
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

class AliexpressView(Categor, ListView):
    model = Aliexpress
    queryset = Aliexpress.objects.all()
    template_name = 'reviews_ali/aliexpress_list.html'

class AliexpressDetail(Categor, DetailView):
    model = Aliexpress
    slug_field = 'url'
    queryset = Aliexpress.objects.all()
    template_name = 'reviews_ali/aliexpress_detail.html'

class SearchAli(Categor, ListView):
    template_name = 'reviews_ali/aliexpress_list.html'

    def get_queryset(self):
        return Aliexpress.objects.filter(title__icontains=self.request.GET.get('search_ali'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search_ali'] = f'searchali={self.request.GET.get("search_ali")}&'
        return context


class FilterCategory(Categor, ListView):
    template_name = 'reviews_ali/filtercategory.html'

    def get_queryset(self):
        queryset = 0
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['videos'] = Reviews.objects.filter(
            category__in=self.request.GET.getlist('category')
        )
        context['alies'] = Aliexpress.objects.filter(
            category__in=self.request.GET.get('category')
        )
        context['newss'] = News.objects.filter(
            category_news__in=self.request.GET.get('category')
        )
        return context