from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import UserRegisterForm

class SignUpView(CreateView):
    form_class = UserRegisterForm
    template_name = "accounts/signup.html"
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        
        return redirect('accounts:dashboard')