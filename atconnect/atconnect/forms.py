from django import forms
from .models import System_Post, Profile
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'bio', 'location','birth_date', 'avatar']
        widgets = {'birth_date': forms.DateInput(attrs={"type":'date'})}
        
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exclude(pk=self.instance.user.pk)
        if user.exists():
            raise ValidationError(_('Email já cadastrado.'))
        return email 