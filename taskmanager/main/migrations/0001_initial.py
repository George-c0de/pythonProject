# Generated by Django 3.2.9 on 2021-12-02 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdUser', models.IntegerField(verbose_name='Id пользователя')),
                ('IdFilm', models.IntegerField(verbose_name='Id фильма')),
            ],
            options={
                'verbose_name': 'Избранно',
                'verbose_name_plural': 'Избранные',
            },
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, verbose_name='Название фильма')),
                ('Grade', models.TextField(verbose_name='Рейтинг')),
                ('Year', models.IntegerField(verbose_name='Год выпуска')),
                ('Imgsmall', models.TextField(verbose_name='Картинка маленькая')),
                ('Imgbig', models.TextField(verbose_name='Картинка большая')),
                ('Class', models.IntegerField(verbose_name='Класс сериала')),
                ('Genre', models.CharField(max_length=30, verbose_name='Жанр фильма')),
                ('Country', models.CharField(max_length=20, verbose_name='Страна производства')),
                ('Season', models.IntegerField(verbose_name='Кол-во сезонов')),
                ('series', models.IntegerField(verbose_name='Кол-во серий ')),
                ('About', models.TextField(verbose_name='О фильме')),
                ('favorites', models.BooleanField(default=False, verbose_name='Избранный')),
                ('viewing', models.BooleanField(default=False, verbose_name='Просмотренный')),
                ('VideoTrailer', models.TextField(verbose_name='трейлер')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, verbose_name='Имя пользователя')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email')),
                ('Password', models.TextField(verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Views',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdUser', models.IntegerField(verbose_name='Id пользователя')),
                ('IdFilm', models.IntegerField(verbose_name='Id фильма')),
            ],
            options={
                'verbose_name': 'Просмотренно',
                'verbose_name_plural': 'Просмотренные',
            },
        ),
    ]
