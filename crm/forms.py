from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput,TextInput
from django.utils.translation import gettext_lazy as _
from . models import Record

class CreateUserForm(UserCreationForm):
     password1 = forms.CharField(
      label=_("Password"),
      widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
  )
     password2 = forms.CharField(
        label=_("Confirm Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
    )
     class Meta:
            model = User
            fields = ('username', 'email', )

            widgets = {
               'username': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Username',
                    'autofocus': "none"
                }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@company.com'
            })
            }

     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    


# create record 

class CreateRecordForm(forms.ModelForm):
     class Meta:
          model = Record

          fields = ['frist_name','last_name','email','phone','address','city','provience','country']
        
          widgets = {
            'frist_name': forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Phone'}),
            'address': forms.Textarea(attrs={'class': 'form-control mt-1', 'placeholder': 'Address', 'rows': 3}),
            'city': forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'City'}),
            'provience': forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Province'}),
            'country': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Country'}),
        }



       

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['frist_name', 'last_name', 'email', 'phone', 'address', 'city', 'provience', 'country']
        
        widgets = {
            'frist_name': forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Phone'}),
            'address': forms.Textarea(attrs={'class': 'form-control mt-1', 'placeholder': 'Address', 'rows': 3}),
            'city': forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'City'}),
            'provience': forms.TextInput(attrs={'class': 'form-control mt-1', 'placeholder': 'Province'}),
            'country': forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Country'}),
        }