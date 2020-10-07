from django.contrib import admin
from .models import InstaLikeBot


class InstaLikeAdmin(admin.ModelAdmin):
    model = InstaLikeBot
    list_display = '__all__'


admin.site.register(InstaLikeBot)
