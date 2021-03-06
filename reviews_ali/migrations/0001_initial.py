# Generated by Django 3.2 on 2021-04-11 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название категории')),
                ('description', models.TextField(verbose_name='Описание категории')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название обзора')),
                ('video_user', models.CharField(max_length=150, verbose_name='Автор обзора')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date_premier', models.DateField(verbose_name='Дата выхода обзора')),
                ('poster', models.ImageField(upload_to='preview/', verbose_name='Превью')),
                ('category', models.ManyToManyField(related_name='review_category', to='reviews_ali.Category', verbose_name='Категории видео')),
            ],
            options={
                'verbose_name': 'Обзор',
                'verbose_name_plural': 'Обзоры',
            },
        ),
    ]
