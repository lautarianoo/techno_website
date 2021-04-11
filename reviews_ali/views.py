from django.shortcuts import render
from django.views.generic import ListView
from .models import News

class Index(ListView):
    #Домашняя страница, список новостей
    model = News
    queryset = News.objects.all()
    template_name = 'reviews_ali/index.html'

