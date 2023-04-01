from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from .forms import SystemForm
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

class ProfileView(View):
    templated_name = 'atconnect/profile.html'
    model = Profile
    context_object_name = 'profile'
    
    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Profile, pk = pk)
    
    def get(self, request, pk):
        profile = self.get_object()
        context = {'profile': profile}
        return render(request, self.templated_name, context)
    
    def post(self, request, pk, *args, **kwargs):
        profile = self.get_object()
        action = request.POST.get('follow')
        if action == 'follow':
            request.user.profile.follows.add(profile)
        elif action == 'unfollow':
            request.user.profile.follows.remove(profile)
        request.user.profile.save()
        profile_pk = request.user.profile.pk
        return redirect(reverse_lazy('atconnect:profile', kwargs={'pk': profile_pk}))
