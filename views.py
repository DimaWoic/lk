from django.shortcuts import render, render_to_response
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import InstaLikeBot
from .forms import BotForm
from django.urls import reverse_lazy


class BotsIndex(ListView):
    template_name = 'instalike/bots_index.html'
    template_name_suffix = '_index'
    context_object_name = 'bots'
    queryset = InstaLikeBot.objects.all()


class BotCreate(CreateView):
    model = InstaLikeBot
    template_name_suffix = '_add'
    success_url = reverse_lazy('bots')
    fields = '__all__'

    def form_invalid(self, form):
        return render_to_response('instalike/error.html')


class BotUpdate(UpdateView):
    model = InstaLikeBot
    template_name_suffix = '_update'
    success_url = reverse_lazy('bots')
    fields = '__all__'

    def get_queryset(self):
        return InstaLikeBot.objects.all()


class DelBot(DeleteView):
    model = InstaLikeBot
    success_url = reverse_lazy('bots')
    context_object_name = 'bot'
