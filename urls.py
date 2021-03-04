from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('logout_done', views.LogOutDone.as_view(), name='logout_done'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('registrations_done/', views.RegisterDoneView.as_view(), name='reg_done'),
    path('change_info/<int:pk>', views.ChangeUserInfoView.as_view(), name='change_info'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_pass'),
    path('change_password_done/', views.ChangePasswordDoneView.as_view(), name='pass_change_done'),
]
