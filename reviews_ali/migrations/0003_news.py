# Generated by Django 3.2 on 2021-04-11 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_ali', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название новости')),
                ('less_description', models.TextField(max_length=300, verbose_name='Краткое описание')),
                ('description', models.TextField(verbose_name='Новость')),
                ('date', models.DateField(verbose_name='Дата выхода новости')),
                ('image', models.ImageField(upload_to='image_news/', verbose_name='Превью новости')),
                ('category_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_category', to='reviews_ali.category', verbose_name='Категории новости')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
