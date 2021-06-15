from django import forms
from django.forms.widgets import EmailInput, PasswordInput

from .models import Emp, Emp_Profile


class Emp_form(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = Emp
        fields = ('emp_name', 'emp_email', 'emp_password')


class Emp_prof_from(forms.ModelForm):
    class Meta():
        model = Emp_Profile
        fields = ('fb_url', 'lk_url', 'profile_pic')


class login1(forms.Form):
    email = forms.EmailField(widget=EmailInput(
        attrs={'class': 'class=input100', 'placeholder': 'Email'}))
    password = forms.CharField(widget=PasswordInput(
        attrs={'class': 'class=input100', 'placeholders': 'Password'}))
