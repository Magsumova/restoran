# Generated by Django 4.0.4 on 2022-05-05 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Названия категорий')),
                ('url', models.URLField(null=True, verbose_name='Иконка категорий')),
            ],
            options={
                'verbose_name': 'Категория блюдо',
                'verbose_name_plural': 'Категорий блюдо',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название блюдо')),
                ('content', models.TextField(verbose_name='О блюдо')),
                ('price', models.IntegerField(verbose_name='Цена блюдо')),
                ('photo', models.URLField(null=True, verbose_name='Фотография блюдо')),
                ('url', models.SlugField(max_length=25, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant_project.category', verbose_name='Категорий блюдо')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
    ]
