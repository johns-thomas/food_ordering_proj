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
    regx_aplha='\A[a-zA-Z]+\Z'
    regx_message='Only Alphabets allowed'
    first_name = forms.CharField(validators=[validators.MinLengthValidator(min_len, min_msg_len),
        validators.MaxLengthValidator(max_len, max_msg_len),validators.RegexValidator(regx_aplha, regx_message)])
    last_name = forms.CharField(validators=[validators.MinLengthValidator(min_len, min_msg_len),
    validators.MaxLengthValidator(max_len, max_msg_len),validators.RegexValidator(regx_aplha, regx_message)])
    email = forms.EmailField(validators=[validators.validate_email])
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['email'].widget.attrs.update({'class': 'form-control'})    
        self.fields['password1'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})  


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

        mobile_validator= validators.RegexValidator(
            regex=r'^\d{10}$', 
            message='Mobile number must contain 10 digits',
        )
        self.fields['phone'].validators.append(mobile_validator)

        address_validator = validators.MinLengthValidator(
            limit_value=6, 
            message='Address should have at least 6 characters.',
        )
        self.fields['daddress'].validators.append(address_validator)

        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        