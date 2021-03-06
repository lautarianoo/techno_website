from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField

class Category(models.Model):
    #Категории
    title = models.CharField('Название категории', max_length=100)
    description = models.TextField('Описание категории')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Reviews(models.Model):
    #Видео/Обзоры/Обучалки
    title = models.CharField('Название обзора', max_length=150)
    video_user = models.CharField('Автор обзора', max_length=150)
    video = models.TextField('Видео')
    description = models.TextField('Описание')
    date_premier = models.DateField('Дата выхода обзора')
    poster = models.ImageField('Превью', upload_to='preview/')
    category = models.ManyToManyField(Category, verbose_name='Категории видео', related_name='review_category')
    url = models.SlugField(max_length=130, unique=True)

    def get_absolute_url(self):
        return reverse("reviews_ali:video_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.feedback_set.filter(parent__isnull=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

class News(models.Model):
    #Новости
    title = models.CharField('Название новости', max_length=100)
    less_description = models.TextField('Краткое описание', max_length=300)
    description = models.TextField('Новость')
    date = models.DateField('Дата выхода новости')
    image = models.ImageField('Превью новости', upload_to='image_news/')
    category_news = models.ForeignKey(Category, verbose_name='Категории новости', related_name='news_category', on_delete=models.CASCADE)
    url = models.SlugField(max_length=130, unique=True)


    def get_absolute_url(self):
        return reverse("reviews_ali:news_detail", kwargs={"slug": self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Feedback(models.Model):
    #Отзывы для видео
    email = models.EmailField()
    video = models.ForeignKey(Reviews, verbose_name='Видео', on_delete=models.CASCADE, null=True)
    name = models.CharField('Имя', max_length=50)
    text = models.TextField(max_length=3000)
    parent = models.ForeignKey('self', verbose_name='Родитель',
                               on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.email} - {self.name}'

    class Meta:
        verbose_name = "Отзыв для видео"
        verbose_name_plural = "Отзывы для видео"


class Aliexpress(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    less_description = models.TextField(max_length=1000)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, verbose_name='Категории', on_delete=models.CASCADE)
    video = models.CharField(max_length=500, blank=True)
    poster = models.ImageField(upload_to='ali_posters/')
    photo = models.ImageField(upload_to='ali_photos/')
    aliurl = models.URLField()
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Али-товар'
        verbose_name_plural = 'Али-товары'
