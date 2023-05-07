from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import UserRegisterForm
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm


class SignUpView(CreateView):
    form_class = UserRegisterForm
    template_name = "accounts/signup.html"
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        
        return redirect('atconnect:dashboard')


def sobre_nos(request):
    return render(request, 'sobre_nos.html')

class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'atconnect/password_reset.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_done')


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'atconnect/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'atconnect/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'atconnect/password_reset_complete.html'