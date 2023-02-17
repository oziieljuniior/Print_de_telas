# Create your views here.

from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Profile, System_Post
from .forms import SystemForm, UserRegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.views import View
from django.core.paginator import Paginator



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

    

def profile_list(request):
    profiles = Profile.objects.all()
    paginator = Paginator(profiles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, "system_list/profile_list.html", context)


def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "system_list/profile.html", {"profile": profile})


def register(request):
    if request.method=='POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seu registro foi criado com sucesso!')
            return HttpResponseRedirect(reverse('login'))
    else:
        form=UserRegisterForm()
    args={'form':form}
    return render(request,'register.html',args)


