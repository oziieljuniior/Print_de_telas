from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import SystemForm, ProfileForm
from .models import System_Post, Profile


# Create your views here.
POSTS_PER_PAGE = 10
class DashboardView(View):
    template_name = 'atconnect/dashboard.html'
    login_url = reverse_lazy('login')
    
    def get(self, request):
        if request.user.is_authenticated:
            form = SystemForm()
            followed_post = System_Post.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by('-created_at')
            return render(request, self.template_name, {'form': form, 'post': followed_post})
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
    profile = request.user.profile
    profile_form = ProfileForm(instance=profile)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('atconnect:profile', pk = profile.pk)
    return render(request, 'atconnect/profile.html',{'profile':profile, 'profile_form':profile_form, 'profile_id':profile.pk})
    