from django import forms
from .models import System_Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SystemForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(
                               attrs={"placeholder": "Post something ...",
                                      "class": "input is-success is-medium",}
                           ),
                           label = "",)
    class Meta:
        model = System_Post
        fields = ("body",)
        widgets = {"user": forms.HiddenInput()}
        
    def save(self, commit = True, user = None):
        instance = super().save(commit=False)
        instance.user = user
        if commit:
            instance.save()
        return instance
    
            
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']