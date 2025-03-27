# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task
from django.contrib.auth import get_user_model

User = get_user_model()

# Form Registrasi
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Enter your email'}),
            'password1' : forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Password'}),
            'password2' : forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Repeat Password'})
        }

# Form Login
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password', ]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date', 'class': 'input-field'}),
            'status': forms.Select(attrs={'class': 'input-field'}),
            'description': forms.Textarea(attrs={'class': 'input-field'}),
            'title': forms.TextInput(attrs={'class': 'input-field'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs['readonly'] = True

class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Enter your email'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No user found with this email.")
        return email
    
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Enter your email'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
