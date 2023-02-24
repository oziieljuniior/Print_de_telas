from django import forms
from .models import System_Post
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
    
            
class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(label='None',max_length=15)
    last_name = forms.CharField(label="Sobrenome",max_length=15)
    email = forms.EmailField(label='E-mail',)
    username = forms.CharField(label='Username', max_length=15)
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email','username','password1','password2')
    
    error_messages = {'invalid_first_character': _('O primeiro caractere deve ser uma letra'),}
    
    def clean(self):
        cleaned_data = super().clean()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if first_name == last_name:
            raise ValidationError(_('Nome e sobrenome não podem ser iguais.'))
        
        if password1 != password2:
            raise ValidationError(_('As senhas devem ser iguais!'))
        
        #return self.cleaned_data
    
    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        
        if data[0].islower():
            raise ValidationError(_('A primeira letra deve ser maiúscula.'))
        
        if data[0].isdigit():
            raise self.get_invalid_first_character_error()

        return data
    
    def get_invalid_first_character_error(self):
        '''
        O primeiro caractere deve ser uma letra.
        '''
        return ValidationError(self.error_messages['invalid_first_character'],code='invalid_first_character')