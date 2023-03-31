# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View


from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import connection

from .models import Profile, System_Post, Mymodel
from .forms import SystemForm, UserRegisterForm

from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.models import User




POSTS_PER_PAGE = 10

#@method_decorator(require_http_methods(["GET"]), name = 'dispatch')
class DashboardView(View):
    template_name = 'system_list/dashboard.html'
    login_url = reverse_lazy('login')
    
    def get(self, request):
        if request.user.is_authenticated:
            form = SystemForm()
            followed_pots = System_Post.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by("-created_at")
            return render(request, self.template_name, {'form': form, 'post': followed_pots})
        else:
            return redirect(self.login_url)
    
    
    #@method_decorator(require_http_methods(["POST"]))
    def post(self, request):
        print(request.method)
        form = SystemForm(request.POST)
        if form.is_valid():
            system = form.save(commit=False)
            system.user = request.user
            system.save()
            return redirect("System_Post:dashboard")
        followed_pots = System_Post.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by("-created_at")
        return render(request, self.template_name, {"form": form, "post": followed_pots})

class ProfileListView(View):
    template_name = 'system_list/profile_list.html'    
    model = Profile
    paginate_by = POSTS_PER_PAGE
    context_object_name = 'profiles'
    
    
    def get_queryset(self):
        return self.model.objects.all().prefetch_related('user')
    
    
    def get(self, request):
        profiles = self.model.objects.exclude(user = request.user)
        context = {'profile_list': profiles}
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        pass
    
    
    

class ProfileView(View):
    template_name = 'system_list/profile.html'
    model = Profile
    context_object_name = 'profile'
    
    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Profile, pk = pk)
    
    def get(self, request, pk):
        profile = self.get_object()
        context = {'profile': profile}
        return render(request, self.template_name, context)
    
    def post(self, request, pk, *args, **kwargs):
        profile = self.get_object()
        action = request.POST.get("follow")
        if action == "follow":
            request.user.profile.follows.add(profile)
        elif action == "unfollow":
            request.user.profile.follows.remove(profile)
        request.user.profile.save()
        profile_pk = request.user.profile.pk
        return redirect(reverse_lazy("System_Post:profile", kwargs={'pk':profile_pk}))

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


class HomePageView(TemplateView, LoginRequiredMixin):
    template_name = 'system_list/home.html'
    
    def dispatch(self, request, **kwargs):
        if request.user.is_authenticated:
            posts = System_Post.objects.all()
            context = {'posts': posts}
            return render(request,self.template_name, context)
        else:
            return redirect(reverse_lazy('login'))
    

class ProfileSearchView(ListView):
    model = Profile
    template_name = 'system_list/profile_search.html'
    context_object_name = 'profiles'
    paginate_by = POSTS_PER_PAGE
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Profile.objects.filter(user__username__icontains=query)
        return Profile.objects.all()
    
class MypasswordResert(PasswordResetView):
    '''
    Classe para resetar senha do usuario
    '''
  
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    
    def form_valid(self, form):
        #Pegar email
        email = form.cleaned_data['email']
        
        #checar se o email existe no sistema
        if User.objects.filter(email=email).exists():
            response = super().form_valid(form)
            
            send_mail('Password Reset Requested', 'Por Favor clique no link abaixo para resetar sua senha', 'oziel.contato@proton.me', [email], fail_silently=False,)
            return response
        
        form.add_error('email','O email fornecido não existe no sistema.')
        return super().form_invalid(form)
    
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

def sobre_nos(request):
    return render(request, 'registration/sobre_nos.html')

