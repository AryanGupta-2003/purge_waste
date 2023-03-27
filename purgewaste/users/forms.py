from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from crispy_forms.helper import FormHelper

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.IntegerField()
    address = forms.CharField()

    class Meta:
        model = User 
        fields = ['username','email','password1','password2','phone','address']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    phone = forms.IntegerField()
    address = forms.CharField()
    class Meta:
        model = User 
        fields = ['username','email','phone','address']
    
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'CurrentProfile'
        

class  ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=  ['image'] 

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'CurrentProfile'


        