# Create your views here.

from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views import View

from .models import Profile, System_Post
from .forms import SystemForm, UserRegisterForm






@login_required
def dashboard(request):
    if request.method == "POST":
        form = SystemForm(request.POST or None)
        if form.is_valid():
            system = form.save(commit=False)
            system.user = request.user
            system.save()
            return redirect("System_Post:dashboard")
    else:
        form = SystemForm()
    followed_pots = System_Post.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by(
        "-created_at")
    return render(request, "system_list/dashboard.html", {"form": form, "post": followed_pots})

class ProfileListView(View):
    templat_name = 'system_list/profile_list.html'    
    model = Profile
    paginate_by = 10
    
    def get(self, request):
        profile = self.model.objects.all().prefetch_related('user')
        paginator = Paginator(profile, self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'page_obj': page_obj}
        return render(request, self.templat_name, context)

class ProfileView(View):
    template_name = 'system_list/profile.html'
    
    def get(self, request, pk):
        if not hasattr(request.user, 'profile'):
            missing_profile = Profile(user = request.user)
            missing_profile.save()
        profile = Profile.objects.select_related('user').get(pk = pk)
        context = {"profile": profile}
        return render(request, self.template_name, context)
    def post(self, request, pk):
        current_user_profile = request.user.profile
        profile = Profile.objects.get(pk = pk)
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
        return redirect(reverse_lazy("System_Post:profile"), kwargs={'pk':pk})

def register(request):
    if request.method=='POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seu registro foi criado com sucesso!')
            return redirect(reverse_lazy('login'))
    else:
        form=UserRegisterForm()
    args={'form':form}
    return render(request,'registration/register.html',args)


