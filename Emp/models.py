from django.db import models
from django.forms.widgets import EmailInput, PasswordInput
from django.forms import ValidationError


class Emp(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=264,blank=False)
    emp_email = models.EmailField(max_length=264,blank=False,unique=True)
    emp_password = models.CharField(max_length=20)

class Emp_Profile(models.Model):
    emp_pro_id = models.ForeignKey(Emp,on_delete=models.CASCADE, default=1)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, default="")
    fb_url = models.URLField(blank=True, default="")
    lk_url = models.URLField(blank=True, default="")

