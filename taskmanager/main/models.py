from django.db import models


class Films(models.Model):
    Name = models.CharField('Название фильма', max_length = 30)
    Grade = models.TextField('Рейтинг')
    Year = models.IntegerField('Год выпуска')
    Imgsmall = models.TextField('Картинка маленькая' )
    Imgbig = models.TextField('Картинка большая')
    Class = models.CharField('Класс сериала', max_length=30) # 1 -фильм, 2- сериал, 3 - мультфильм
    Genre = models.CharField('Жанр фильма', max_length=30)
    Country = models.CharField('Страна производства', max_length=20)
    Season = models.IntegerField('Кол-во сезонов', default=0)
    series = models.IntegerField('Кол-во серий ', default=0)
    About = models.TextField('О фильме')
    favorites = models.BooleanField('Избранный', default=False)
    viewing = models.BooleanField('Просмотренный', default=False)
    VideoTrailer = models.TextField('трейлер')

    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class User(models.Model):
    Name = models.CharField('Имя пользователя', max_length=30)
    Email = models.EmailField('Email')
    Password = models.TextField('Пароль')

    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Favorite(models.Model):
    IdUser = models.IntegerField('Id пользователя')
    IdFilm = models.IntegerField('Id фильма')


    def __str__(self):
        return self.IdUser

    class Meta:
        verbose_name = 'Избранно'
        verbose_name_plural = 'Избранные'


class Views(models.Model):
    IdUser = models.IntegerField('Id пользователя')
    IdFilm = models.IntegerField('Id фильма')


    class Meta:
        verbose_name = 'Просмотренно'
        verbose_name_plural = 'Просмотренные'


