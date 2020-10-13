from django.shortcuts import render, render_to_response
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, TemplateView
from .models import InstaLikeBot
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from django.contrib.auth.views import LoginView, LogoutView

def main_page(request):
    return render(request, template_name='instalike/base/base.html')


class RegistrationView(CreateView):
    form_class = forms.RegForm
    template_name = 'instalike/registration.html'
    success_url = reverse_lazy('reg_done')


class UserLoginView(LoginView):
    template_name = 'instalike/login.html'


class UserLogoutView(LogoutView, LoginRequiredMixin):
    next_page = 'logout_done'


class LogOutDone(TemplateView):
    template_name = 'instalike/logout.html'


class RegisterDoneView(TemplateView):
    template_name = 'instalike/register_done.html'


class BotsIndex(ListView, LoginRequiredMixin):
    login_url = 'login'
    redirect_field_name = 'main'
    template_name = 'instalike/bots_index.html'
    template_name_suffix = '_index'
    context_object_name = 'bots'
    queryset = InstaLikeBot.objects.all()


class BotCreate(CreateView, LoginRequiredMixin):
    login_url = 'login'
    redirect_field_name = 'main'
    model = InstaLikeBot
    template_name_suffix = '_add'
    success_url = reverse_lazy('bots')
    fields = '__all__'

    def form_invalid(self, form):
        return render_to_response('instalike/error.html')


class BotUpdate(UpdateView, LoginRequiredMixin):
    login_url = 'login'
    redirect_field_name = 'main'
    model = InstaLikeBot
    template_name_suffix = '_update'
    success_url = reverse_lazy('bots')
    fields = '__all__'

    def get_queryset(self):
        return InstaLikeBot.objects.all()


class DelBot(DeleteView, LoginRequiredMixin):
    login_url = 'login'
    redirect_field_name = 'main'
    model = InstaLikeBot
    success_url = reverse_lazy('bots')
    context_object_name = 'bot'
