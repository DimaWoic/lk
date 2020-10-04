from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from instapy import InstaPy
import os


class InstaLikeBot(models.Model):
    is_active = models.BooleanField(verbose_name='Бот активен', default=False)
    name = models.CharField(verbose_name='Имя бота')
    login = models.CharField(verbose_name='логин')
    password = models.CharField(verbose_name='пароль')
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


def like_bot(login, password, peak_likes_h, peak_likes_daily, like_tags, like_posts, random, rel_enable, rel_max_follow, dont_like):
    path = os.getcwd() + '/geckodriver'
    session = InstaPy(username=login, password=password, geckodriver_path=path, headless_browser=True)
    session.login()
    session.set_quota_supervisor(enabled=True, peak_likes_hourly=peak_likes_h, peak_likes_daily=peak_likes_daily)
    session.like_by_tags([like_tags], amount=like_posts, randomize=random)
    session.set_relationship_bounds(enabled=rel_enable, max_followers=rel_max_follow)
    session.set_dont_like([dont_like])
    session.end()

@receiver(post_save, InstaLikeBot)
def start_bot():
    bot = InstaLikeBot()
    if bot.is_active == True:
        like_bot(bot.login, bot.password, bot.peak_likes_h, bot.peak_likes_d, bot.like_tags, bot.like_posts,
                 bot.random, bot.relashionships_enable, bot.relashionships_max_follow, bot.dont_like)


