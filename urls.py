from django.urls import path
from . import views
from django.contrib.auth import views as aviews


urlpatterns = [
    #path('', views.BotsIndex.as_view(), name='bots'),
    #path('del_bot/<int:pk>', views.DelBot.as_view(), name='del_bot'),
    #path('add_bot', views.BotCreate.as_view(), name='add_bot'),
    #path('bot_update/<int:pk>', views.BotUpdate.as_view(), name='bot_update'),
    path('', views.main_page, name='main'),
    path('login/', aviews.LoginView.as_view(), name='login'),
    path('logout/', aviews.LogoutView.as_view(), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
]
