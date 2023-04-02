from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# creating a form classes
class LoginForm(AuthenticationForm):
    # customising form fields
    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'username',
            'class': 'form-control',
            'id': 'floatingInput',
        
        }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'password',
            'class': 'form-control',
            'id': 'floatingInput',
        
        }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # customising form fields
    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'username',
            'class': 'form-control',
            'id': 'floatingInput',
        
        }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
            'placeholder': 'name@example.com',
            'class': 'form-control',
            'id': 'floatingInput',
        
        }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'password',
            'class': 'form-control',
            'id': 'floatingInput',
        
        }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'passeord',
            'class': 'form-control',
            'id': 'floatingInput',
        
        }))
