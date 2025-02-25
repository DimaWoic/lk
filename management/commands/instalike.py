from django.core.management.base import BaseCommand
import os
import gevent


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
