from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as views
from accounts.views import RegisterView, HomePageView, ProfileView, settings, help, faq, about, contact, sobre_nos


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('accounts.urls')),
    path('home/', HomePageView.as_view(), name="home"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", views.LogoutView.as_view(), name = "logout"),
    path("login/", views.LoginView.as_view(), name = "login"),
    path("settings/", settings, name = "settings"),
    path('help/', help, name = 'help'),
    path('help/faq', faq, name = 'faq'),
    path('help/about', about, name = 'about'),
    path('contact/', contact, name = 'contact'),
    path('sobre-nos/', sobre_nos, name = 'sobre_nos'),
    path('reset-password-sent/', views.PasswordResetDoneView.as_view(template_name = 'registration/password_reset_done.html'), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('reset_password_complete/', views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'), name = 'password_reset_complete'),
]
