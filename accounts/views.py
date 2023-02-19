# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.db.models import Q 

from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connection



from .models import Profile, System_Post, Mymodel
from .forms import SystemForm, UserRegisterForm




POSTS_PER_PAGE = 10

@method_decorator(require_http_methods(["GET"]), name = 'dispatch')
class DashboardView(View):
    template_name = 'system_list/dashboard.html'
    
    def get(self, request):
        form = SystemForm()
        followed_pots = System_Post.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by(
            "-created_at")
        return render(request, self.template_name, {'form': form, 'post': followed_pots})
    
    @method_decorator(require_http_methods(["POST"]))
    def post(self, request):
        form = SystemForm(request.POST or None)
        if form.is_valid():
            system = form.save(commit=False)
            system.user = request.user
            system.save()
            return redirect("System_Post:dashboard")
        followed_pots = System_Post.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by("-created_at")
        return render(request, self.template_name, {"form": form, "post": followed_pots})

class ProfileListView(View):
    templat_name = 'system_list/profile_list.html'    
    model = Profile
    paginate_by = POSTS_PER_PAGE
    context_object_name = 'profiles'
    
    
    def get_queryset(self):
        return self.model.objects.all().prefetch_related('user')
    
    
    def get(self, request):
        profiles = self.get_queryset()
        context = {'profile_list': profiles}
        return render(request, self.templat_name, context)
        
    def post(self, request, *args, **kwargs):
        pass
    
    
    

class ProfileView(View):
    template_name = 'system_list/profile.html'
    model = Profile
    context_object_name = 'profile'
    
    def post(self, request, pk, *args, **kwargs):
        profile = self.get_object()
        action = request.POST.get("follow")
        if action == "follow":
            request.user.profile.follows.add(profile)
        elif action == "unfollow":
            request.user.profile.follows.remove(profile)
        request.user.profile.save()
        return redirect(reverse_lazy("System_Post:profile"), kwargs={'pk':profile.pk})

class RegisterView(View):
    template_name = 'registration/register.html'
    
    def get(self,request):
        form = UserRegisterForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seu registro foi criado com sucesso!')
            return redirect(reverse_lazy('login'))
    
        args={'form':form}
        return render(request,self.template_name,args)


class MyModelView(View):
    template_name = 'system_list/my_template.html'
    def get(self,request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM odds")
            rows = cursor.fetchall()
        context = {'data': rows}
        return render(request, self.template_name, context)
    

class HomePageView(TemplateView):
    template_name = 'system_list/home.html'
    
def settings(request):
    return render(request, 'system_list/settings.html')

def help(request):
    return render(request, "help/help.html")

def about(request):
    return render(request, "help/about.html")
def faq(request):
    return render(request, "help/faq.html")

def contact(request):
    return render(request, 'help/contact.html')