from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import SystemForm, ProfileForm
from .models import System_Post, Profile
from datetime import datetime
from django.views.generic import ListView
from django.db import connection


# Create your views here.
POSTS_PER_PAGE = 10
class DashboardView(View):
    template_name = 'atconnect/dashboard.html'
    login_url = reverse_lazy('accounts:login')
    
    def get(self, request):
        if request.user.is_authenticated:
            form = SystemForm()
            year = datetime.now().year
            followed_post = System_Post.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by('-created_at')
            return render(request, self.template_name, {'year': year, 'form': form, 'post': followed_post})
        else:
            return redirect(self.login_url)    

    def post(self, request):
        print(request.method)
        form = SystemForm(request.POST)
        if form.is_valid():
            system = form.save(commit=False)
            system.user = request.user
            system.save()
            return redirect('atconnect:dashboard')
        followed_posts = System_Post.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by('-created_at')
        return render(request, self.template_name, {'form':form, 'post':followed_posts})

@login_required
def ProfileView(request, pk):
    profile = None
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        pass

    if profile is None:
        # Redireciona o usuário para a página de criação de perfil
        return redirect('atconnect:create_profile')
        
    profile_form = ProfileForm(instance=profile)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('atconnect:profile', pk=profile.pk)
    return render(request, 'atconnect/profile.html', {'profile': profile, 'profile_form': profile_form, 'profile_id': profile.pk})

class ProfileSearchVIew(ListView):
    model = Profile
    template_name = 'atconnect/profile_search.html'
    context_object_name = 'profiles'
    paginate_by = POSTS_PER_PAGE
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Profile.objects.filter(user__username__icontains=query)
        return Profile.objects.all()
    
class MyModelView(View):
    template_name = 'atconnect/my_tamplate.html'
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM odds")
            rows = cursor.fetchall()
        context = {'data': rows}
        return render(request, self.template_name, context)