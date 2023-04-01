from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .forms import SystemForm

# Create your views here.
POSTS_PER_PAGE = 10
class DashboardView(View):
    template_name = 'atconnect/dashboard.html'
    login_url = reverse_lazy('login')
    
    def get(self, request):
        if request.user.is_authenticated:
            form = SystemForm()
