from django.core.management.base import BaseCommand
from instalike.models import InstaLikeBot
from instapy import InstaPy
import os


def like_bot(login, password, peak_likes_h, peak_likes_daily, like_tags, like_posts, random, rel_enable, rel_max_follow, dont_like):
    path = os.getcwd() + '/instalike/geckodriver'
    print(path)
    session = InstaPy(username=login, password=password, geckodriver_path=path, headless_browser=True)
    session.login()
    session.set_quota_supervisor(enabled=True, peak_likes_hourly=peak_likes_h, peak_likes_daily=peak_likes_daily)
    session.like_by_tags([like_tags], amount=like_posts, randomize=random)
    session.set_relationship_bounds(enabled=rel_enable, max_followers=rel_max_follow)
    session.set_dont_like([dont_like])
    session.end()


class Command(BaseCommand):

    def handle(self, *args, **options):
        bots = InstaLikeBot.objects.all()
        for bot in bots:
            if bot.is_active:
                like_bot(bot.login, bot.password, bot.peak_likes_h, bot.peak_likes_d, bot.like_tags, bot.like_posts,
                         bot.random, bot.relashionships_enable, bot.relashionships_max_follow, bot.dont_like)
