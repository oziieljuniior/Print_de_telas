from django import forms
from .models import System_Post
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email

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
