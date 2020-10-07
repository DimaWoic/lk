from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class InstaLikeBot(models.Model):
    is_active = models.BooleanField(verbose_name='Бот активен', default=False)
    name = models.CharField(verbose_name='Имя бота', max_length=255, unique=True)
    login = models.CharField(verbose_name='логин', max_length=255)
    password = models.CharField(verbose_name='пароль', max_length=255)
    peak_likes_h = models.IntegerField(default=0, verbose_name='максимальное количество лайков в час')
    peak_likes_d = models.IntegerField(default=0, verbose_name='максимальное количество лайков в день')
    like_tags = models.TextField(verbose_name='теги')
    like_posts = models.IntegerField(default=0, verbose_name='количество лайкнутых постов')
    random = models.BooleanField(default=True, verbose_name='Рандомный выбор постов')
    relashionships_enable = models.BooleanField(default=False, verbose_name='Ограничить посты аккаунтов')
    relashionships_max_follow = models.IntegerField(default=0, verbose_name='Максимальное количество подписчиков аккаунта')
    dont_like = models.TextField(verbose_name='Не лайкать по тегам')

    class Meta:
        verbose_name = 'Лайк бот'
        verbose_name_plural = 'Лайк_боты'

    def __str__(self):
        return self.name

