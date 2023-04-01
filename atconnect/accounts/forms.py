from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
    
            
class UserRegisterForm(UserCreationForm, forms.ModelForm):
    """ 
    Formulário de registro de usuário.
    """
    
    first_name = forms.CharField(label='None',max_length=15, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}))
    last_name = forms.CharField(label="Sobrenome",max_length=15)
    email = forms.EmailField(label='E-mail')
    
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email','username','password1','password2')
    
    error_messages = {'invalid_first_character': _('O primeiro caractere deve ser uma letra'),}
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            field.widget.attrs.update({'placeholder': field.label})
    
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
        
        #chama todas as validações do campo
        return cleaned_data
        
    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError(_("Senha deve ter mais do que 7 caracteres"))
        return password1
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError(_("Username utilizado. Tente outro"))
        return username
    
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
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError(_('Endereço de e-mail inválido'))
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_('Este endereço de e-mail já está em uso.'))
        
        return email
    
    def save(self, commit=True):
        #Usa self.instance para atualizar o objeto existente
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user