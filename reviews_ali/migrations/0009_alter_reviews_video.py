# Generated by Django 3.2 on 2021-04-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_ali', '0008_auto_20210412_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='video',
            field=models.TextField(verbose_name='Видео'),
        ),
    ]
