from django.core.management.base import BaseCommand
from instalike.models import InstaLikeBot
from instapy import InstaPy
import os
import gevent


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


def bots_i(i):
    bots = InstaLikeBot.objects.all()
    if bots[i].is_active:
        like_bot(bots[i].login, bots[i].password, bots[i].peak_likes_h, bots[i].peak_likes_d, bots[i].like_tags, bots[i].like_posts,
                 bots[i].random, bots[i].relashionships_enable, bots[i].relashionships_max_follow, bots[i].dont_like)
        gevent.sleep(0)


class Command(BaseCommand):

    def handle(self, *args, **options):
        bots = InstaLikeBot.objects.all()
        index = len(bots) - 1
        if index < 0:
            pass
        else:
            list_bots = []
            if index == 0:
                bots_i(0)
            for i in range(index):
                list_bots.append(gevent.spawn(bots_i(i)))

            gevent.joinall(list_bots)
            print(index)
