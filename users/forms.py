from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class CreateUserForm(UserCreationForm):
    min_len = 2
    max_len = 20
    min_msg_len = f"Minimum {min_len} characters long."
    max_msg_len = f"Maximum {max_len} characters long."
    first_name = forms.CharField(validators=[validators.MinLengthValidator(min_len, min_msg_len),
        validators.MaxLengthValidator(max_len, max_msg_len)])
    last_name = forms.CharField(validators=[validators.MinLengthValidator(min_len, min_msg_len),
    validators.MaxLengthValidator(max_len, max_msg_len)])
    email = forms.EmailField(validators=[validators.validate_email])
    
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('daddress', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['daddress'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        